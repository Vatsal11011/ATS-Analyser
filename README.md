# AI Resume–Job Description Analyzer (ATS System)

An AI-driven Applicant Tracking System (ATS) built using **Gemini Pro Vision** and **Streamlit** to analyze resumes against job descriptions.  
The system parses resumes directly from PDF files using multimodal AI, performs structured resume–JD comparison, and generates **KPI-based match scores** along with skill gap analysis and recruiter-style feedback.

---

## 🚀 Features

- 📄 **Multimodal Resume Parsing**  
  Extracts structured information from PDF resumes using Gemini Pro Vision (PDF → image → AI extraction)

- 🔍 **Resume–Job Description Matching**  
  Compares candidate profiles against job descriptions using skill, experience, and tool alignment

- 📊 **KPI-Based Scoring System**
  - Overall ATS Match Percentage  
  - Skill Match %
  - Experience Match %
  - Tools & Technology Match %

- 🧠 **Skill Gap & Missing Keyword Analysis**  
  Identifies missing or weak keywords that may impact ATS ranking

- 🖥️ **Interactive Dashboard**  
  Streamlit-based UI for real-time resume evaluation and insights

---

## 🧱 System Architecture

1. **Input Layer**
   - Resume uploaded as PDF
   - Job Description entered as text

2. **ETL Pipeline**
   - **Extract:** Resume content parsed via Gemini Pro Vision  
   - **Transform:** Skill normalization and structured entity mapping  
   - **Load/Analyze:** Resume–JD comparison and scoring

3. **Analysis Layer**
   - KPI-based scoring logic
   - Recruiter-style evaluation and feedback

4. **Visualization Layer**
   - Streamlit dashboard with match metrics and results

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Streamlit  
- **AI Model:** Gemini Pro Vision  
- **PDF Processing:** pdf2image, PIL  
- **Environment Management:** python-dotenv  

---
