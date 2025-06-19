
# 🎬 YouTube Video Summarizer (LLM-based)

This project lets you **paste any YouTube video URL** and get a **short AI-generated summary** along with the **full transcript** — powered by `facebook/bart-large-cnn` (Hugging Face Transformers) and an intuitive Gradio interface.

### 🌟 Features
- ✅ Fetches YouTube transcripts using `youtube_transcript_api`
- ✅ Summarizes using Hugging Face’s BART model (`facebook/bart-large-cnn`)
- ✅ Chunks long text intelligently to handle model token limits
- ✅ Clean, minimal Gradio UI with dark theme
- ✅ Displays both summary and full transcript for reference

---

### 🚀 Demo

> Coming soon: Live demo on Hugging Face Spaces!  
> Until then, run locally with the steps below 👇

---

### 📦 Installation

```bash
git clone https://github.com/Tanujasontakke/youtube-video-summarizer.git
cd youtube-video-summarizer
python -m venv venv
source venv/bin/activate  # Or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
