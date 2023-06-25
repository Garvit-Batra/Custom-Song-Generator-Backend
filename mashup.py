import os
import subprocess
import sys
from pydub import AudioSegment
import json


def downloadSongs(search_query, start_time, end_time):
    url = search_query
    if not os.path.exists('songs'):
        os.makedirs('songs')
    subprocess.run(['yt-dlp', url, "--extract-audio", "--audio-format", "mp3", "-o",
                   f"songs/%(title)s.%(ext)s", "--postprocessor-args", f"-ss {start_time} -t {end_time - start_time}"])


def main():
    json_string = sys.argv[1]
    json_object = json.loads(json_string)
    for i in range(len(json_object)):
        downloadSongs(json_object[i]["link"], int(
            json_object[i]["st"]), int(json_object[i]["et"]))


if __name__ == "__main__":
    main()
