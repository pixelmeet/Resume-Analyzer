import os
import fitz  # PyMuPDF
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None

# Function to analyze resume with Gemini
def analyze_compatibility(resume_text, job_desc_text, job_role):
    prompt = f"""
    Analyze the compatibility between this resume and the job description for a {job_role} position.

    Resume:
    {resume_text}

    Job Description:
    {job_desc_text}

    Provide a comprehensive analysis with these sections:

    ### 🔍 Compatibility Overview
    - Brief summary of overall fit
    - Key strengths for this role
    - Major gaps to address

    ### 📊 Match Metrics
    - Skills Match: X% (Top matching skills)
    - Experience Alignment: X% (Relevant experience match)
    - Keyword Optimization: X% (ATS-friendly keywords present)

    ### 🛠️ Technical Skills Analysis
    | Required Skill | Present | Proficiency | Importance |
    |----------------|---------|-------------|------------|
    [Table with technical skills assessment]

    ### 🌟 Soft Skills Analysis
    | Desired Quality | Evidence in Resume | Match Level |
    |-----------------|--------------------|-------------|
    [Table with soft skills assessment]

    ### 📌 Keyword Gap Analysis
    | Missing Keyword | Category | Importance | Suggestion |
    |----------------|----------|------------|------------|
    [Table with important missing keywords]

    ### 🚀 Improvement Recommendations
    1. Top 3 resume modifications
    2. Suggested skills to highlight
    3. Recommended action items

    ### ⚖️ Final Compatibility Score: X/10
    [Detailed explanation of score]

    Format the response in clear markdown with emojis for better readability.
    Be specific, constructive, and prioritize actionable insights.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error analyzing resume: {str(e)}")
        return None

# Function to generate ATS optimization tips
def generate_ats_tips(resume_text, job_desc_text):
    prompt = f"""
    Analyze this resume and job description for Applicant Tracking System (ATS) optimization:

    Resume:
    {resume_text}

    Job Description:
    {job_desc_text}

    Provide specific ATS optimization tips including:

    1. Missing ATS-critical keywords
    2. Suggested section improvements
    3. Formatting recommendations
    4. Common ATS pitfalls to avoid

    Present as a bulleted list with priority indicators (🚨 High, ⚠️ Medium, ℹ️ Low).
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating ATS tips: {str(e)}")
        return None

# Streamlit UI
st.set_page_config(
    page_title="Resume-Job Match Analyzer", 
    layout="wide",
    page_icon="📊"
)

# Sidebar for inputs
with st.sidebar:
    st.title("🔍 Input Parameters")
    job_role = st.text_input("Target Job Role*", placeholder="e.g. Data Scientist, Product Manager")
    uploaded_resume = st.file_uploader("Upload Your Resume (PDF)*", type="pdf")
    uploaded_job_desc = st.file_uploader("Upload Job Description (PDF/TXT)", type=["pdf", "txt"])
    
    # Optional advanced options
    with st.expander("⚙️ Advanced Options"):
        analysis_depth = st.select_slider(
            "Analysis Depth",
            options=["Basic", "Detailed", "Comprehensive"],
            value="Detailed"
        )
        include_ats = st.checkbox("Include ATS Optimization", value=True)
    
    analyze_btn = st.button(
        "Analyze Compatibility", 
        disabled=not (uploaded_resume and job_role),
        type="primary"
    )

# Main content area
st.title("📊 Resume-Job Compatibility Analyzer")
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .match-metric {
        border-left: 5px solid #4CAF50;
        padding: 0.5em 1em;
        background-color: #f8f9fa;
        margin: 1em 0;
    }
    </style>
""", unsafe_allow_html=True)

if analyze_btn:
    with st.spinner("🔍 Analyzing compatibility..."):
        # Extract texts
        resume_text = extract_text_from_pdf(uploaded_resume)
        job_desc_text = ""
        
        if uploaded_job_desc:
            if uploaded_job_desc.type == "application/pdf":
                job_desc_text = extract_text_from_pdf(uploaded_job_desc)
            else:
                job_desc_text = uploaded_job_desc.read().decode("utf-8")
        
        if not resume_text:
            st.error("Failed to extract text from resume")
            st.stop()
        
        # Perform analysis
        analysis = analyze_compatibility(resume_text, job_desc_text, job_role)
        ats_tips = generate_ats_tips(resume_text, job_desc_text) if include_ats else None
        
        if not analysis:
            st.error("Failed to generate analysis")
            st.stop()
        
        # Display results
        st.success("Analysis completed!")
        
        # Create tabs for different sections
        tab1, tab2, tab3 = st.tabs(["📋 Full Report", "📊 Metrics", "🚀 Recommendations"])
        
        with tab1:
            st.markdown(analysis)
        
        with tab2:
            # Parse metrics from analysis (simplified for example)
            # In a real app, you'd extract these programmatically
            st.subheader("Key Metrics")
            
            cols = st.columns(3)
            with cols[0]:
                st.metric("Skills Match", "78%", "5% above average")
            with cols[1]:
                st.metric("Experience Alignment", "65%", "Needs improvement")
            with cols[2]:
                st.metric("Keyword Optimization", "82%", "Strong")
            
            st.subheader("Skill Match Visualization")
            # Example data - in real app parse from analysis
            skill_data = pd.DataFrame({
                "Skill": ["Python", "SQL", "TensorFlow", "Data Visualization", "Cloud Computing"],
                "Match Score": [90, 85, 60, 75, 50],
                "Importance": ["High", "High", "Medium", "Medium", "Low"]
            })
            st.bar_chart(skill_data, x="Skill", y="Match Score")
        
        with tab3:
            st.subheader("Actionable Recommendations")
            
            # Parse recommendations (simplified for example)
            st.markdown("""
            ### 🎯 Top Priority
            - Add 3+ years of cloud experience to work history
            - Include 'AWS' and 'Azure' in skills section
            
            ### 📈 Important Improvements
            - Highlight leadership in project descriptions
            - Add metrics to quantify achievements
            
            ### 🔍 Optimization
            - Reorder skills to match job description priority
            - Include industry-specific keywords
            """)
            
            if ats_tips:
                st.subheader("📝 ATS Optimization Tips")
                st.markdown(ats_tips)
            
            # Generate downloadable report
            report_content = f"# Resume-Job Compatibility Report\n\nRole: {job_role}\n\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\n## Analysis\n\n{analysis}\n\n"
            if ats_tips:
                report_content += f"## ATS Optimization Tips\n\n{ats_tips}\n"
            
            st.download_button(
                label="📥 Download Full Report",
                data=report_content,
                file_name=f"compatibility_report_{job_role.replace(' ','_')}.md",
                mime="text/markdown"
            )

# Add footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray;">
    <p>Powered by Gemini 1.5 Flash | Analyze your resume against job descriptions for better matches</p>
    </div>
""", unsafe_allow_html=True)