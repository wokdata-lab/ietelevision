import random

base = "https://ietelevision.wokdata.group/canal/"

videos = [
"video1.ts",
"video2.ts",
"video3.ts",
"video4.ts",
"video5.ts"
]

random.shuffle(videos)

out = "#EXTM3U\n"

for v in videos:
    out += "#EXTINF:300,\n"
    out += base + v + "\n"

open("ietelevision.m3u8","w").write(out)
