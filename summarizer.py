from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_transcript(video_url):
    try:
        video_id = video_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        return " ".join([entry['text'] for entry in transcript])
    except NoTranscriptFound:
        return "Error English transcript not found. Try another video."
    except TranscriptsDisabled:
        return "Error Transcripts are disabled for this video."
    except Exception as e:
        return f"Error: {str(e)}"

def chunk_text(text, max_words=500):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def summarize_chunks(chunks):
    all_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1} of {len(chunks)}...")
        summary = summarizer(chunk, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
        all_summaries.append(summary)
    return " ".join(all_summaries)

# Test it
if __name__ == "__main__":
    # Step 1: Get URL from user
    url = input("Enter YouTube video URL: ")

    # Step 2: Extract transcript
    text = get_transcript(url)

    # Step 3: Handle error or proceed
    if text.startswith("❌"):
        print(text)
    else:
        # Step 4: Chunk transcript
        chunks = chunk_text(text)
        print(f"✅ Transcript retrieved. Number of chunks: {len(chunks)}")

        # Step 5: Summarize
        final_summary = summarize_chunks(chunks)

        # Step 6: Print final output
        print("\n=== 📄 Final Summary ===\n")
        print(final_summary)

