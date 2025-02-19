import json
from pathlib import Path
from pprint import pprint

def get_transcript(volume):
    mokuro_path = volume.path_mokuro
    # get transcript
    print("Getting transcript...")

    vol_title = volume.name
    print(vol_title)
    volume_txt = ""
    with open(f"{mokuro_path}", 'r', encoding="UTF-8") as vol_mokuro:
        vol_mokuro = json.load(vol_mokuro)

    for page in vol_mokuro['pages']:
        volume_txt += page['img_path'] + '\n'
        for block in page['blocks']:
            txt = "".join(block['lines'])
            volume_txt += txt + '\n\n'
    
    with open(f"{volume.path_title}\\{vol_title}_transcript.txt", 'w', encoding="UTF-8") as transcript:
        transcript.write(volume_txt)

    print("Transcript created.")