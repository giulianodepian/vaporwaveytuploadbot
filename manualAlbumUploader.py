
import videocreator
import os
import shutil
import re
from pathlib import Path

import sys

def createVideoDescription(tracksTimestamps, listOfTracks):
    i = 0
    videoDescription = ""
    for trackName in listOfTracks:
        videoDescription += trackName + " " + formatTimeStamps(tracksTimestamps[i]) + "\n"
        i += 1
    print(videoDescription)
    return videoDescription

def formatTimeStamps(timeStamp):
    minutes = timeStamp // 60
    seconds = timeStamp % 60
    hour = 0
    
    if (minutes >= 60):
        tempMinutes = minutes
        minutes = minutes % 60
    
        while (tempMinutes >= 60):
            hour += 1
            tempMinutes = tempMinutes / 60
    
    if (hour > 0):
        return str(hour) + ":" + "{:02d}".format(int(minutes)) + ":" + "{:02d}".format(int(seconds))
    
    return str(minutes) + ":" + "{:02d}".format(int(seconds))

def getTrackList(id):
    p = Path(id)
    trackList = []
    for audio in p.glob("*.flac"):
        trackName = re.search(r'- \d\d .*(?=.flac)', str(audio))
        if not trackName:
            trackName = re.search(r'\d\d .*(?=.flac)', str(audio))
        trackList.append(trackName.group(0))
    trackList.sort()
    return trackList

with open("albumListManual.txt", encoding="utf8") as albumList:
    for id in albumList:
        formattedId = id.strip()
        try:
            listOfTracks = getTrackList(formattedId)
            tracksTimestamps = videocreator.createAlbumVideo(formattedId, listOfTracks)
            descFile = open(f'desc {formattedId}.txt', 'w', encoding="utf8")
            descFile.write(createVideoDescription(tracksTimestamps, listOfTracks))
            descFile.close()
        except Exception as e:
            print("Album " + formattedId + f' Failed!: {e}')