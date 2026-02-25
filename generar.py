import random

base = "https://ietelevision.wokdata.group/canal/"

videos = [
"video1.ts",
"video2.ts",
"video3.ts",
"video4.ts",
"video5.ts"
]

videos = videos * 30
random.shuffle(videos)

out = "#EXTM3U\n\n"

for v in videos:
    out += "#EXTINF:600,\n"
    out += base + v + "\n\n"

open("ietelevision.m3u8","w").write(out)
