import re, glob
filename = re.sub("_0_.*?$", "", glob.glob("*_0_*.mp3")[0])
for i in range(200):
    with open(f"{filename}.m3u", "a") as fileObj:
        if glob.glob(f"*_{i}_*.mp3"):
            fileObj.write(glob.glob(f"*_{i}_*.mp3")[0]+"\r")
