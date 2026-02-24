import random

base = "https://ietelevision.wokdata.group/stream/"

videos = [
base + "video1/video1.m3u8",
base + "video2/video2.m3u8",
base + "video3/video3.m3u8"
]

random.shuffle(videos)

out = "#EXTM3U\n"
out += "#EXT-X-VERSION:3\n"

for i in range(100):
    for v in videos:
        out += "#EXT-X-STREAM-INF:BANDWIDTH=3000000\n"
        out += v + "\n"

with open("ietelevision.m3u8","w") as f:
    f.write(out)
