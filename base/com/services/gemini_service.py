import os
from google import genai
from base import GEMINI_API_KEY

def parse_resume(extracted_resume_text):
    client_genai = genai.Client(api_key=GEMINI_API_KEY)
    response = client_genai.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"""
                    You are an expert resume parser. Extract the following details from this resume text:
                    - Full Name
                    - Email
                    - Phone Number
                    - Skills (list)
                    - Education (list of objects degree, institution, start_date, end_date, cgpa, percentage)
                    - Work Experience (list of objects with title, company, description, start_date, end_date or empty list if not present) 
                    - Projects (list of objects with title, description, github_link, start_date, end_date)

                    **Important:**  
                        • Do NOT include any bullet characters (e.g. “•”) in your JSON.  
                        • Normalize any ligatures (e.g. “ﬁ” → “fi”).  
                        • Return flat JSON arrays and strings only—no leading symbols or special punctuation.

                    Return the output keys: name, email, phone, location, skills, education, experience, projects.
                    in just ''' '''
                    Resume Text:
                    {extracted_resume_text}

                    ps: ignore
                    """, 
        config={"response_mime_type": "application/json"}
    )

    print(response.text)
    parsed_json_data = response.text
    return parsed_json_data