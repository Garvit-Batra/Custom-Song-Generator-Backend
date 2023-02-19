import os
import subprocess
import sys
from pydub import AudioSegment

def downloadSongs(search_query,start_time,end_time):
    url = search_query
    if not os.path.exists('songs'):
        os.makedirs('songs')
    subprocess.run(['yt-dlp',url,"--extract-audio","--audio-format", "mp3", "-o", f"songs/%(title)s.%(ext)s", "--postprocessor-args", f"-ss {start_time} -t {end_time - start_time}"])

def main():
    search_query = sys.argv[1]
    start_time = int(sys.argv[2])
    end_time = int(sys.argv[3])
    downloadSongs(search_query,start_time,end_time)

if __name__ == "__main__":
    main()