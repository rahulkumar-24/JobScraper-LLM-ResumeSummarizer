Yes 👍 your README is already **clear, well-structured, and professional** — it explains your project, shows installation steps, and includes screenshots for visual proof.

Just a few **small improvements** I’d suggest:

* Fix minor formatting issues in code blocks (`\_` escaping and closing backticks count).
* Make the repository name in the clone command match your folder name.
* Add a short “How It Works” section so visitors understand the flow in 30 seconds.

Here’s a slightly cleaned-up version of your README:

---

```markdown
# 📄 AI Job Recommender

An AI-powered job recommendation tool that extracts information from your resume, summarizes your profile, identifies skill gaps, and fetches relevant job listings from platforms like LinkedIn and Naukri.  
It leverages advanced scraping APIs and intelligent matching to help you find jobs that align with your skills and plan your next career step.

---

## 🚀 Features

- **Resume Parsing** – Extracts skills and experience from uploaded PDF resumes.
- **Resume Summarization** – Generates a concise summary of your professional background.
- **Skill Gap Analysis** – Compares your skills with job requirements to identify missing skills.
- **AI Career Guidance** – Suggests the next steps to improve your profile for better job matches.
- **Multi-Platform Job Fetching** – Finds jobs from LinkedIn, Naukri, and other platforms.
- **Streamlit Web App** – User-friendly interface for quick job recommendations.
- **Real-time Scraping** – Powered by Scrapdog API and Apify Client for live job data.

---

## 🛠️ Tech Stack & Libraries Used

- **[Streamlit](https://streamlit.io/)** – Web application framework for building the UI.
- **[PyMuPDF](https://pymupdf.readthedocs.io/)** – PDF parsing and text extraction.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** – Environment variable management.
- **[apify-client](https://docs.apify.com/api/client/python)** – Fetch job data from Apify actors.
- **Scrapdog API** – For scraping LinkedIn job data efficiently.

---

## 📂 Project Structure

```

project/
│── src/
│   ├── helper.py               # Functions for PDF parsing, AI summarization & skill gap analysis
│   ├── fetch\_job.py             # Fetch job data from APIs
│── screenshot/                  # Project screenshots
│   ├── Resume\_Upload\_Feedback.png
│   ├── Job\_Recommendation.png
│── .env                         # API keys & environment variables
│── app.py                       # Main Streamlit application
│── requirements.txt             # Project dependencies
│── README.md                    # Project documentation

````

---

## ⚙️ Installation & Setup

1. Clone the repository

   git clone https://github.com/rahulkumar-24/JobScraper-LLM-ResumeSummarizer.git
   cd JobScraper-LLM-ResumeSummarizer


2. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Setup environment variables

   * Create a `.env` file in the root directory.
   * Add your API keys:

     ```
     SCRAPDOG_API_KEY=your_scrapdog_api_key
     APIFY_API_TOKEN=your_apify_api_token
     GEMINI_API_KEY=your_gemini_api_key
     ```

5. Run the application

   ```bash
   streamlit run app.py
   ```

---

## 📸 Screenshots

### 📄 Resume Upload & Summary

After uploading your resume, the application parses the data, generates a summary, and identifies skill gaps.

![Resume Upload Feedback](screenshot/Resume_Upload_Feedback.png)

---

### 💼 Job Recommendations

Based on your parsed skills, the system recommends the most relevant jobs from LinkedIn, Naukri, and other sources.

![Job Recommendation](screenshot/Job_Recommendation.png)

---

## 📜 License

This project is licensed under the MIT License.

---

## ✨ Author

Rahul Kumar
📧 [rahulkumar.19k8@gmail.com](mailto:rahulkumar.19k8@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/rahulkumar19k8/)


