import gradio as gr
from summarizer import get_transcript, chunk_text, summarize_chunks

def summarize_video(url):
    transcript = get_transcript(url)
    if not transcript:
        return "Transcript not available.", ""

    chunks = chunk_text(transcript)
    summary = summarize_chunks(chunks)
    return summary, transcript

iface = gr.Interface(
    fn=summarize_video,
    inputs=gr.Textbox(label="🎥 Enter YouTube Video URL"),
    outputs=[
        gr.Textbox(label="🔍 AI Summary"),
        gr.Textbox(label="📜 Full Transcript")
    ],
    title="🧠 YouTube Video Summarizer",
    description="Paste a YouTube link to get a short summary + full transcript.",
    theme="Base",  # <<< Add this line for dark theme
    article="Created with ❤️ by Tanuja — Code on GitHub: https://github.com/Tanujasontakke/youtube-video-summarizer"
)

if __name__ == "__main__":
    iface.launch(inbrowser=True, share=True)
