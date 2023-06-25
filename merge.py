import os
import sys
from pydub import AudioSegment


def mergeSongs(output_file):
    folder_path = "songs"
    items = []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            creation_time = entry.stat().st_ctime
            items.append((entry.name, creation_time))

    sorted_items = sorted(items, key=lambda x: x[1])

    merged_audio = AudioSegment.empty()
    folder = "songs"
    for song in sorted_items:
        song_path = f"{folder}/{song[0]}"
        audio_segment = AudioSegment.from_file(song_path, format="mp3")
        merged_audio += audio_segment

    merged_audio.export(output_file, format="mp3")


def main():
    output_file = sys.argv[1]
    mergeSongs(output_file)


if __name__ == "__main__":
    main()
