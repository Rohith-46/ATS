import os
import pdfplumber
from groq import Groq

client = Groq(api_key=os.getenv("RESUME_ANALYZER_GROQ_API_KEY"))

def analyze_resume(resume_text: str):
    try:

        response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
"content": f"""You are an expert ATS recruiter and career coach.

Analyze the resume below and return **only** a valid JSON object. Do not include any explanations, markdown, or extra text outside the JSON.

Resume Text:
{resume_text}

Return the response in this exact JSON format:

{{
  "overall_score": <integer between 0 and 100>,
  "ats_compatibility_score": <integer between 0 and 100>,
  "strengths": ["strength 1", "strength 2", "strength 3", "strength 4"],
  "improvements": ["improvement 1", "improvement 2", "improvement 3", "improvement 4"],
  "missing_keywords": ["keyword1", "keyword2", "keyword3"]
}}

Now analyze the resume and fill the JSON with real insights based on the content."""
        }],
        temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
        
    except Exception as e :
            return False
    

def Convert_pdf_into_text(file):
    text = "" 
    try :
        with pdfplumber.open(file) as pdf:
            for pages in pdf.pages:
                page_text = pages.extract_text()
                if page_text:
                    text += page_text+"\n"
                return text.strip()
    except Exception as e:
        return None

