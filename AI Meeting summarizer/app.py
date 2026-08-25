import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

meeting_text = """
Project Meeting

John: We will launch the website on Monday.
Sarah: I will complete the UI today.
David: Backend testing will finish tomorrow.
Everyone agreed to conduct the final review on Friday.
"""

prompt = f"""
Summarize the following meeting and provide:

1. Summary
2. Key Points
3. Action Items
4. Decisions

Meeting:
{meeting_text}
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)