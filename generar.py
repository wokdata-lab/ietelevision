import random

base = "https://ietelevision.wokdata.group/canal/"

videos = [
"video1.ts",
"video2.ts",
"video3.ts",
"video4.ts",
"video5.ts"
]

# duplicamos la lista para que dure más
videos = videos * 40

# mezclar
random.shuffle(videos)

m3u = "#EXTM3U\n"
m3u += "#EXT-X-VERSION:3\n"
m3u += "#EXT-X-TARGETDURATION:3600\n\n"

for v in videos:
    m3u += "#EXTINF:-1,\n"
    m3u += base + v + "\n"

open("ietelevision.m3u8","w").write(m3u)
