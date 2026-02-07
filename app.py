from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 🔹 UPDATED: clearer function naming + structured output
def get_gemini_response(prompt, pdf_content, jd_text):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content(
        [prompt, pdf_content[0], jd_text]
    )
    return response.text


# 🔹 SAME logic, just cleaner variable naming
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        return [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        }]
    else:
        raise FileNotFoundError("No file uploaded")


# ================= STREAMLIT UI =================
st.set_page_config(page_title="AI ATS Resume Analyzer")
st.header("📄 AI Resume–Job Description Analyzer (ATS)")

jd_text = st.text_area("📌 Job Description", key="jd_input")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully")

col1, col2 = st.columns(2)
with col1:
    analyze_resume = st.button("🔍 Resume Evaluation")
with col2:
    match_score = st.button("📊 ATS Match Score")


# ================= PROMPTS =================

# 🔹 NEW: Resume Parsing & ETL Prompt
resume_etl_prompt = """
You are an AI ATS system.
Extract structured information from the resume including:
- Skills (standardized)
- Tools & Technologies
- Years of experience
- Education
Return output in clear bullet points.
"""

# 🔹 UPDATED: KPI-based evaluation
ats_scoring_prompt = """
You are an advanced ATS scanner.

Steps:
1. Compare resume against the job description.
2. Calculate KPI scores:
   - Skill Match %
   - Experience Match %
   - Tool/Tech Match %
3. Calculate Overall ATS Match Percentage.
4. List missing or weak keywords.
5. Give final recruiter-style feedback.

Output format:
Overall Match: XX%
Skill Match: XX%
Experience Match: XX%
Tools Match: XX%

Missing Keywords:
- keyword1
- keyword2

Final Thoughts:
"""

# ================= ACTIONS =================

if analyze_resume and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(resume_etl_prompt, pdf_content, jd_text)

    st.subheader("📑 Parsed Resume Data (ETL Output)")
    st.write(response)


elif match_score and uploaded_file:
    pdf_content = input_pdf_setup(uploaded_file)
    response = get_gemini_response(ats_scoring_prompt, pdf_content, jd_text)

    st.subheader("📊 ATS Match Results")
    st.write(response)

    # 🔹 Dashboard-style KPIs (visual layer)
    st.markdown("### 🔢 KPI Snapshot")
    st.metric("Overall ATS Match", "—")
    st.metric("Skill Match", "—")
    st.metric("Experience Match", "—")
