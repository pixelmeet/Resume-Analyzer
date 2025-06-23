# Resume-Analyzer

A simple web tool that helps you compare your resume to any job description—no technical skills needed! Powered by Google Gemini AI, it gives you easy-to-understand feedback, shows how well your resume matches the job, and offers tips to improve your chances, whether you're applying for a job in business, healthcare, education, the arts, or any other field.

## Who is this for?
Anyone looking for a job! This tool is designed for people from all backgrounds—not just tech. Whether you're a teacher, nurse, manager, artist, or engineer, Resume-Analyzer can help you make your resume stand out for any job.

## What does it do?
- **Upload Your Resume & Job Description**: Just upload your resume (PDF) and the job description (PDF or text).
- **Get a Simple Analysis**: The tool checks how well your resume matches the job, highlights your strengths, and points out areas to improve.
- **See Easy-to-Read Scores**: Find out how closely your skills and experience match the job requirements.
- **Get Actionable Tips**: Receive clear suggestions to make your resume better and more likely to get noticed.
- **ATS Tips**: Learn how to make your resume more likely to pass automated systems used by employers.
- **Download Your Report**: Save the feedback as a file you can keep or share.

## Example
> **You're applying for a Marketing Manager job.**
> Upload your resume and the job description. The tool will show you which marketing skills you have, which ones you might want to add, and give you tips (like using certain keywords or highlighting teamwork experience) to improve your chances.

## How to Use
1. **Prepare your files:**
   - Your resume (PDF format)
   - The job description (PDF or text file)
2. **Start the app:**
   - Open a terminal or command prompt
   - Run: `streamlit run resume_analyzer.py`
   - The app will open in your web browser
3. **Follow the steps on the screen:**
   - Upload your resume and job description
   - Enter the job title you're applying for (e.g., "Marketing Manager", "Teacher", "Nurse")
   - (Optional) Adjust the analysis settings if you want
   - Click the button to analyze
4. **Read your results:**
   - See your match scores, strengths, and improvement tips
   - Download the full report if you want

## What do I need?
- **No coding or technical skills required!**
- A computer with Python 3.8 or higher
- Internet access
- A free API key from [Google Gemini](https://ai.google.dev/) (instructions below)

## Quick Setup
1. **Install Python** (if you don't have it): [Download Python](https://www.python.org/downloads/)
2. **Install the required packages:**
   ```bash
   pip install streamlit python-dotenv google-generativeai pymupdf pandas
   ```
3. **Get your Google Gemini API key:**
   - Sign up at [Google Gemini](https://ai.google.dev/)
   - Copy your API key
   - Create a file named `.env` in the project folder and add this line:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
4. **Start the app:**
   ```bash
   streamlit run resume_analyzer.py
   ```

## Frequently Asked Questions
**Q: Do I need to know how to code?**
> No! You just need to follow the steps above.

**Q: Does this work for non-technical jobs?**
> Yes! It works for any job or field.

**Q: Is my data safe?**
> Your files are only used for the analysis and are not shared.

## License
[MIT](LICENSE)

## Acknowledgements
- Powered by [Google Gemini](https://ai.google.dev/)
- Built with [Streamlit](https://streamlit.io/)