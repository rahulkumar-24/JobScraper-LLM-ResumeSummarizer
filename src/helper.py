import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get Gemini API key
GEMINI_API_KEY = os.getenv("Gemini_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (file): The uploaded PDF file object.
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text



