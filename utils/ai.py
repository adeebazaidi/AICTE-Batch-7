import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

def generate_professional_summary(name, title, skills, experience, education, projects):
    """Generates a professional 2-4 sentence summary using Gemini."""
    client = get_client()
    if not client:
        return "Error: GEMINI_API_KEY is missing."

    prompt = f"""
    Write a highly professional and engaging 2-4 sentence resume summary for the following professional:
    
    Name: {name}
    Title: {title}
    Skills: {skills}
    Experience: {experience}
    Education: {education}
    Projects: {projects}
    
    The summary should highlight their key strengths, experience level, and what they bring to a team. 
    It must be ATS-friendly, concise, written in the third-person or implied first-person (e.g., "Results-driven software engineer..."), and avoid generic buzzwords.
    Do NOT output anything else besides the summary itself.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def generate_cover_letter(name, job_role, skills, experience):
    """Generates a cover letter tailored to a specific job role."""
    client = get_client()
    if not client:
        return "Error: GEMINI_API_KEY is missing."

    prompt = f"""
    Write a professional and compelling cover letter for {name} applying for the position of {job_role}.
    
    Here is their background information:
    Skills: {skills}
    Experience: {experience}
    
    The cover letter should be structured professionally, with a strong opening, a body paragraph highlighting relevant skills and experiences, and a confident closing call to action.
    Do not include placeholder text like "[Date]" or "[Hiring Manager Name]"—just output the main body content directly starting with "Dear Hiring Manager,".
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error generating cover letter: {str(e)}"
