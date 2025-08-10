import pdfplumber
from googletrans import Translator
import os

def translate_pdf_text(pdf_path):
    """
    Extracts text from a PDF, translates it to English, gets a simulated LLM response,
    and translates the response back to Malayalam.

    Args:
        pdf_path (str): The path to the PDF file.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    # 1. Extract text from the PDF
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                full_text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return

    if not full_text.strip():
        print("No text could be extracted from the PDF.")
        return

    print("--- Extracted Malayalam Text ---")
    print(full_text)

    translator = Translator()

    # 2. Translate the extracted text from Malayalam to English
    try:
        translated_to_english = translator.translate(full_text, src='ml', dest='en')
        print("\n--- Translated to English ---")
        print(translated_to_english.text)
    except Exception as e:
        print(f"Error translating to English: {e}")
        return

    # 3. Simulate feeding the English text to an LLM and getting a response
    llm_response_english = f"This is a simulated LLM response to the following English text: '{translated_to_english.text}'"
    print("\n--- Simulated LLM Response (English) ---")
    print(llm_response_english)

    # 4. Translate the English response back to Malayalam
    try:
        final_response_malayalam = translator.translate(llm_response_english, src='en', dest='ml')
        print("\n--- Final Response (Malayalam) ---")
        print(final_response_malayalam.text)
    except Exception as e:
        print(f"Error translating back to Malayalam: {e}")
        return

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        translate_pdf_text(pdf_path)
    else:
        print("Please provide the path to a Malayalam PDF file as a command-line argument.")
        print("Example: python malayalam_translator.py your_pdf.pdf")
