import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(prompt):

    response = model.generate_content(prompt)

    text = response.text

    # remove markdown JSON formatting if present
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()