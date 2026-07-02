# AI Resume Builder (v2.0)

A highly polished, premium SaaS-style web application that helps users dynamically build, preview, and export professional resumes and AI-generated cover letters. Powered by Streamlit, Google Gemini AI, and WeasyPrint.

## ✨ Features (v2.0 Updates)
- **Premium UI/UX:** A stunning interface featuring glassmorphism, floating drop-shadows, smooth CSS animations, and a curated professional color palette.
- **Live A4 Preview:** See your resume update in real-time on a floating, perfectly scaled A4 page right next to your form.
- **Multiple Professional Templates:** Choose from 'Modern Clean', 'Minimal Premium', or 'Two Column' layouts to best fit your industry.
- **State Persistence (Auto-Save):** Never lose your work. Your data is automatically saved to a local state file and persists even if you accidentally refresh the page.
- **Pixel-Perfect PDF Export:** Instantly convert your live resume preview into a high-quality PDF ready for recruiters.
- **AI Integration (Google Gemini):** Use the power of AI to instantly generate professional summaries and tailored cover letters with a single click.

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adeebazaidi/AICTE-Batch-7.git
   cd AICTE-Batch-7
   ```

2. **Add your Gemini API key:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

3. **Install dependencies:**
   Make sure you have Python 3.8+ installed. Note: PDF generation relies on `weasyprint`, which may require you to install GTK3 on Windows/Mac.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python -m streamlit run app.py
   ```

## 🎨 Technologies Used
- **Frontend/Framework:** Streamlit, Custom HTML/CSS
- **Backend AI:** Google `google-generativeai` (Gemini API)
- **PDF Generation:** WeasyPrint / PDFKit
- **Styling:** Vanilla CSS injected via Streamlit components, featuring the 'Inter' Google Font.

## 📦 Deployment
This app can be deployed quickly and natively on **Streamlit Cloud**, **Render**, or **Heroku**.
