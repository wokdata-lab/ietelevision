import random
import os

base_url = "https://ietelevision.wokdata.group/stream/"
base_path = "stream"

segments = []

for root, dirs, files in os.walk(base_path):
    for f in files:
        if f.endswith(".ts"):
            path = root.replace("\\", "/") + "/" + f
            segments.append(path)

random.shuffle(segments)

playlist = "#EXTM3U\n"
playlist += "#EXT-X-VERSION:3\n"
playlist += "#EXT-X-TARGETDURATION:7\n"
playlist += "#EXT-X-MEDIA-SEQUENCE:0\n"

for i in range(2000):
    for seg in segments:
        playlist += "#EXTINF:6.0,\n"
        playlist += base_url + seg + "\n"

with open("ietelevision.m3u8", "w") as f:
    f.write(playlist)
