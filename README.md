# 📊 Resume-Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Streamlit-Enabled-orange.svg" alt="Streamlit"/>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/banner.png" alt="Resume Analyzer Banner" width="80%"/>
</p>

> **🚀 Quick Start**
> 
> 1. **Clone the repository:**
>    ```bash
>    git clone https://github.com/pixelmeet/Resume-Analyzer.git
>    cd Resume-Analyzer
>    ```
> 2. **Install dependencies:**
>    ```bash
>    pip install streamlit python-dotenv google-generativeai pymupdf pandas
>    ```
> 3. **Set up your API key:**
>    - Get a free API key from [Google Gemini](https://ai.google.dev/)
>    - Create a file named `.env` in the project folder and add:
>      ```
>      GEMINI_API_KEY=your_gemini_api_key_here
>      ```
> 4. **Run the app:**
>    ```bash
>    streamlit run resume_analyzer.py
>    ```

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Key Features](#-key-features)
- [Who Can Use This?](#-who-can-use-this)
- [How It Works](#-how-it-works)
- [Quick Start Guide](#-quick-start-guide)
- [Step-by-Step Usage](#-step-by-step-usage)
- [FAQ](#-frequently-asked-questions)
- [License & Acknowledgements](#-license--acknowledgements)

---

## 📝 Overview
Resume-Analyzer helps you understand how well your resume matches a job description. It highlights your strengths, suggests improvements, and gives you tips to make your resume stand out—no matter your background or the job you want.

---

## ✨ Key Features
- 📄 **Easy Uploads:** Add your resume (PDF) and job description (PDF or text).
- 🤖 **AI-Powered Analysis:** Get a simple, clear report on your fit for the job.
- 📊 **Match Scores:** See how your skills and experience align with the job.
- 💡 **Actionable Tips:** Get suggestions to improve your resume and boost your chances.
- 🏆 **ATS Optimization:** Learn how to pass automated resume screeners.
- 📥 **Downloadable Report:** Save your results as a file.

---

## 👥 Who Can Use This?
- **Anyone applying for a job!**
- Works for all fields: marketing, teaching, nursing, management, engineering, arts, and more.
- No coding or technical experience required.

---

## ⚙️ How It Works
1. **Upload your resume and job description.**
2. **Enter the job title you're applying for.**
3. **Click to analyze.**
4. **Read your personalized report and download it if you wish.**

**Example:**
> Applying for a Marketing Manager job? Upload your resume and the job description. The tool will show which marketing skills you have, which ones to add, and give you tips (like using certain keywords or highlighting teamwork) to improve your chances.

---

## 🚀 Quick Start Guide
**Prerequisites:**
- 🐍 Python 3.8 or higher
- 🌐 Internet access
- 🔑 Free API key from [Google Gemini](https://ai.google.dev/)

**Installation:**
1. **Install Python** ([Download here](https://www.python.org/downloads/))
2. **Install required packages:**
   ```bash
   pip install streamlit python-dotenv google-generativeai pymupdf pandas
   ```
3. **Get your Gemini API key:**
   - Sign up at [Google Gemini](https://ai.google.dev/)
   - Copy your API key
   - Create a file named `.env` in the project folder and add:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
4. **Start the app:**
   ```bash
   streamlit run resume_analyzer.py
   ```

---

## 🖱️ Step-by-Step Usage
1. **Prepare your files:**
   - Resume (PDF)
   - Job description (PDF or text)
2. **Open the app in your browser.**
3. **Follow the on-screen instructions:**
   - Upload your files
   - Enter the job title (e.g., "Marketing Manager", "Teacher", "Nurse")
   - (Optional) Adjust analysis settings
   - Click "Analyze Compatibility"
4. **View your results:**
   - See your match scores, strengths, and improvement tips
   - Download the full report if you want

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>Do I need to know how to code?</strong></summary>
No! Just follow the steps above.
</details>

<details>
<summary><strong>Does this work for non-technical jobs?</strong></summary>
Yes! It works for any job or field.
</details>

<details>
<summary><strong>Is my data safe?</strong></summary>
Your files are only used for the analysis and are not shared.
</details>

---

## 📄 License & Acknowledgements
- **License:** [MIT](LICENSE)
- **Powered by:** [Google Gemini](https://ai.google.dev/)
- **Built with:** [Streamlit](https://streamlit.io/)