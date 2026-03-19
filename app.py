import streamlit as st
import PyPDF2

# Skill list
skills_list = [
    "python", "java", "machine learning", "data analysis",
    "sql", "react", "ai", "deep learning", "html", "css"
]

# Extract text from PDF
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

# Extract skills
def extract_skills(text):
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

# UI
st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and get smart suggestions 🚀")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)
    skills = extract_skills(text)

    st.success("Resume analyzed successfully!")

    # Skills
    st.subheader("✅ Extracted Skills")
    st.write(skills)

    # Score
    score = min(len(skills) * 10, 100)
    st.subheader("🎯 Resume Score")
    st.write(score, "/ 100")
    st.progress(score)

    # Suggestions
    st.subheader("📈 Suggestions")

    if "machine learning" not in skills:
        st.write("- Add Machine Learning projects")
    if "react" not in skills:
        st.write("- Learn React for frontend development")
    if "sql" not in skills:
        st.write("- Improve database knowledge")
    if "python" not in skills:
        st.write("- Add Python projects")

    st.info("Keep improving your resume to increase your chances 🚀")
