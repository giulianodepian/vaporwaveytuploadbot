
import videocreator
import os
import shutil
import re
from pathlib import Path

import sys

def createVideoDescription(tracksTimestamps, id):
    p = Path(id)
    i = 0
    videoDescription = ""
    for audio in p.glob("*.flac"):
        trackName = re.search(r'- \d\d .*(?=.flac)', str(audio))
        if not trackName:
            trackName = re.search(r'\d\d .*(?=.flac)', str(audio))
        videoDescription += trackName.group(0) + " " + formatTimeStamps(tracksTimestamps[i]) + "\n"
        i += 1
    print(videoDescription)
    return videoDescription

def formatTimeStamps(timeStamp):
    minutes = timeStamp // 60
    seconds = timeStamp % 60
    
    return str(minutes) + ":" + "{:02d}".format(int(seconds))

with open("albumListManual.txt", encoding="utf8") as albumList:
    for id in albumList:
        formattedId = id.strip()
        try:
            tracksTimestamps = videocreator.createAlbumVideo(formattedId)
            descFile = open(f'desc {formattedId}.txt', 'w', encoding="utf8")
            descFile.write(createVideoDescription(tracksTimestamps, formattedId))
            descFile.close()
        except Exception as e:
            print("Album " + formattedId + f' Failed!: {e}')
            if Path(formattedId).is_dir():
                shutil.rmtree(id, ignore_errors=True)
            ##if Path(id + ".mp4").is_file():
                ##os.remove(id + ".mp4")