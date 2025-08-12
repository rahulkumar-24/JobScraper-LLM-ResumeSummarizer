import os
import streamlit as st
from dotenv import load_dotenv
from src.helper import extract_text_from_pdf
from src.fetch_job import fetch_linkedin_jobs, fetch_naukri_jobs
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------- LOAD ENV VARIABLES ----------------
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("Gemini_API_KEY")  # Load API key from .env

# ---------------- INITIALIZE MODEL ONCE ----------------
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

def ask_langchain(prompt_text, variables=None, max_tokens=500):
    """
    Uses LangChain with Gemini 2.0 Flash to process prompts.
    variables: dict for PromptTemplate variables
    """
    if variables is None:
        variables = {}
    
    prompt = PromptTemplate(
        input_variables=list(variables.keys()),
        template=prompt_text
    )
    chain = prompt | llm
    result = chain.invoke(variables)
    return result.content

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="🚀 AI Job Recommender", layout="wide")
st.title("📄 AI Job Recommender")
st.markdown("✨ *Upload your resume and let AI recommend the best jobs for you from LinkedIn & Naukri!* ✨")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📂 **Upload your resume (PDF)**", type=["pdf"])

if uploaded_file:
    with st.spinner("⏳ Extracting text from your resume... 📄"):
        resume_text = extract_text_from_pdf(uploaded_file)

    # Resume Summary
    with st.spinner("📝 Summarizing your resume... ✨"):
        summary = ask_langchain(
            "Summarize this resume highlighting the skills, education, and experience:\n\n{resume_text}",
            variables={"resume_text": resume_text},
            max_tokens=500
        )

    # Skill Gaps
    with st.spinner("🔍 Finding skill gaps... 🛠️"):
        gaps = ask_langchain(
            "Analyze this resume and highlight missing skills, certifications, and experiences needed for better job opportunities:\n\n{resume_text}",
            variables={"resume_text": resume_text},
            max_tokens=400
        )

    # Roadmap
    with st.spinner("📈 Creating your future career roadmap... 🚀"):
        roadmap = ask_langchain(
            "Based on this resume, suggest a future roadmap to improve career prospects (Skills to learn, certifications, industry exposure):\n\n{resume_text}",
            variables={"resume_text": resume_text},
            max_tokens=400
        )

    # ---------------- RESULTS DISPLAY ----------------
    def display_card(title, icon, content):
        st.markdown(f"### {icon} {title}")
        st.markdown(
            f"<div style='background-color: #1e1e1e; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{content}</div>",
            unsafe_allow_html=True
        )
        st.markdown("---")

    display_card("Resume Summary", "📑", summary)
    display_card("Skill Gaps & Missing Areas", "🛠️", gaps)
    display_card("Future Roadmap & Strategy", "🚀", roadmap)

    st.success("✅ Analysis Completed Successfully!")

    # ---------------- JOB RECOMMENDATION ----------------
    if st.button("🔎 Get Job Recommendations"):
        with st.spinner("🤖 Analyzing your profile & generating job keywords... 🔍"):
            keywords = ask_langchain(
                """
                You are a career advisor. Based on the resume summary below, generate a highly relevant,
                comma-separated list of specific job titles that match the candidate’s skills, work experience,
                industry background, and education.

                Resume Summary:
                {summary}
                """,
                variables={"summary": summary},
                max_tokens=150
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"🎯 **Job Keywords Identified:** {search_keywords_clean}")

        with st.spinner("📡 Fetching jobs from LinkedIn and Naukri... 🌐"):
            first_keyword = search_keywords_clean.split(",")[0].strip()
            linkedin_jobs = fetch_linkedin_jobs(first_keyword)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean)

        # ---------------- JOB DISPLAY FUNCTION ----------------
        def display_job_card(title, company, location, extra_info, link, logo_url=None):
            st.markdown("<div style='border:1px solid #444; border-radius:10px; padding:10px; margin-bottom:10px;'>", unsafe_allow_html=True)
            col1, col2 = st.columns([1, 4])
            with col1:
                if logo_url:
                    st.image(logo_url, width=60)
                else:
                    st.markdown("🗂️")
            with col2:
                st.markdown(f"**{title}** at *{company}*")
                st.markdown(f"- 📍 {location}")
                for info in extra_info:
                    st.markdown(info)
                st.markdown(f"- 🔗 [Apply Here]({link})")
            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- NAUKRI JOBS ----------------
        st.markdown("## 💼 Top Naukri Jobs (India)")
        if naukri_jobs:
            for job in naukri_jobs:
                extra_info = []
                if job.get("salary"):
                    extra_info.append(f"- 💰 {job.get('salary')}")
                if job.get("jobDescription"):
                    extra_info.append(f"- 📝 {job.get('jobDescription')}")
                display_job_card(
                    job.get('title', 'N/A'),
                    job.get('companyName', 'Unknown'),
                    job.get('location', 'Not specified'),
                    extra_info,
                    job.get('jdURL', '#'),
                    job.get('logoPath')
                )
        else:
            st.warning("⚠️ No Naukri jobs found.")

        # ---------------- LINKEDIN JOBS ----------------
        st.markdown("## 💼 Top LinkedIn Jobs")
        if linkedin_jobs:
            for job in linkedin_jobs:
                extra_info = [
                    f"- 🕒 {job.get('job_posting_date', 'Date not available')}"
                ]
                if job.get("job_description"):
                    extra_info.append(f"- 📝 {job.get('job_description')}")
                display_job_card(
                    job.get('job_position', 'N/A'),
                    job.get('company_name', 'Unknown'),
                    job.get('job_location', 'Not specified'),
                    extra_info,
                    job.get('job_link', '#'),
                    job.get('company_logo_url')
                )
        else:
            st.warning("⚠️ No LinkedIn jobs found.")
