"""
place images in folder `images`
"""

import os

cwd = os.getcwd()
for i in os.listdir("images"):
    image_file_path = os.path.join(cwd, "images", i)
    audio_file_path = ""
    for ii in os.listdir():
        if ii.startswith(f"{i[:-4]}_") and ii.endswith(".mp3"):
            audio_file_path = os.path.join(cwd, ii)
            break
    if audio_file_path:
        video_file_path = audio_file_path.replace(".mp3", ".mp4")
        if not os.path.isfile(video_file_path):
            cli = f'''ffmpeg -loop 1 -i "{image_file_path}" -i "{audio_file_path}" -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest {video_file_path}'''
            os.system(cli)
