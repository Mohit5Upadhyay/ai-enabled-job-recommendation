import fitz # PyMuPDF
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
ENDPOINT = os.getenv("ENDPOINT")
os.environ["ENDPOINT"] = ENDPOINT
client = OpenAI(api_key=OPENAI_API_KEY,base_url=ENDPOINT)

# extract content form PDF file
def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text from the PDF.
    """

    doc = fitz.open(stream=uploaded_file.read(),filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()
    return text



def ask_openai(prompt, max_tokens=300):
    """
    Sends a prompt to the OpenAI API and returns the response.
    
    Args:
        prompt (str): The prompt to send to the OpenAI API.
        model (str): The model to use for the request.
        temperature (float): The temperature for the response.
        
    Returns:
        str: The response from the OpenAI API.
    """

    response = client.chat.completions.create(
        model= "openai/gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
