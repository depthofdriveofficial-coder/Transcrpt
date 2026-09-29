from youtube_transcript_api import YouTubeTranscriptApi

video_id = "3jnWlmI3un8"

api = YouTubeTranscriptApi()
transcript = api.fetch(video_id)

with open("transcript.txt", "w", encoding="utf-8") as f:
    for entry in transcript:
        f.write(f"[{entry.start:.2f}s] {entry.text}\n")

print("Transcript saved successfully!")
