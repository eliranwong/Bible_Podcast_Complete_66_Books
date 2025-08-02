import os
from pydub import AudioSegment

for f in os.listdir():
    if os.path.isdir(f):
        for i in os.listdir(f):
            if i.startswith("."):
                print(i)
                os.remove(os.path.join(os.getcwd(), f, i))
                continue
            j = i.replace(" ", "_").replace(",", "").replace("'", "_").replace("__", "_")
            os.rename(os.path.join(os.getcwd(), f, i), os.path.join(os.getcwd(), f, j))
            if i.endswith(".wav"):
                wav_file = os.path.join(os.getcwd(), f, j)
                mp3_file = os.path.splitext(wav_file)[0] + ".mp3"
                audio = AudioSegment.from_wav(wav_file)
                album = f'Bible Podcast - {f}'
                audio.export(mp3_file, format="mp3", tags={'artist': 'SearchBible.AI', 'album': album, 'title': i[:-4], 'comments': 'https://searchbible.ai', 'year': '2025'})
                try:
                    os.remove(wav_file)
                except:
                    pass