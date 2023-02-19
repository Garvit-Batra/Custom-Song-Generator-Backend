import os
import sys
from pydub import AudioSegment

def mergeSongs(output_file):
    folder = "songs"
    audio_files = [f for f in os.listdir(folder) if f.endswith('.mp3')]
    merged_audio = AudioSegment.from_mp3(os.path.join(folder, audio_files[0]))
    for audio_file in audio_files[1:]:
        audio = AudioSegment.from_mp3(os.path.join(folder, audio_file))
        merged_audio = merged_audio + audio
    merged_audio.export(output_file, format="mp3")

def main():
    output_file = sys.argv[1]
    mergeSongs(output_file)

if __name__ == "__main__":
    main()