import random

base = "https://ietelevision.wokdata.group/stream/"

videos = [
base + "video1/video1.m3u8",
base + "video2/video2.m3u8",
base + "video3/video3.m3u8"
]

random.shuffle(videos)

contenido = "#EXTM3U\n"

for i in range(50):
    for v in videos:
        contenido += "#EXTINF:-1,IETelevision\n"
        contenido += v + "\n"
        contenido += "#EXT-X-DISCONTINUITY\n"

with open("ietelevision.m3u8","w") as f:
    f.write(contenido)
