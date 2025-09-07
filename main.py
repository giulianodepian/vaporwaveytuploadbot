import archivedownloader
import videocreator
import youtubeuploader
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

with open("albumList.txt") as albumList:
    youtube = youtubeuploader.get_authenticated_service()
    for album in albumList:
        formattedId = album.strip()
        try:
            archivedownloader.downloadAlbum(formattedId)
            listOfTracks = getTrackList(formattedId)
            tracksTimestamps = videocreator.createAlbumVideo(formattedId, listOfTracks)
            youtubeuploader.uploadAlbum(youtube, formattedId, archivedownloader.getAlbumTitleAndCreator(formattedId), createVideoDescription(tracksTimestamps, listOfTracks))
            os.remove(formattedId + ".mp4")
            shutil.rmtree(formattedId, ignore_errors=True)  
        except Exception as e:
            print("Album " + formattedId + f' Failed!: {e}')
            ##if Path(formattedId).is_dir():
                ##shutil.rmtree(formattedId, ignore_errors=True)
            ##if Path(formattedId + ".mp4").is_file():
                ##os.remove(formattedId + ".mp4")

