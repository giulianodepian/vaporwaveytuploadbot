import archivedownloader
import videocreator
import youtubeuploader
import os
import shutil
import re
from pathlib import Path

def createVideoDescription(tracksTimestamps, id):
    p = Path(id)
    i = 0
    videoDescription = ""
    for audio in p.glob("*.flac"):
        videoDescription += re.search(r'- \d\d .*(?=.flac)', str(audio)).group(0) + " " + formatTimeStamps(tracksTimestamps[i]) + "\n"
        i += 1
    print(videoDescription)
    return videoDescription

def formatTimeStamps(timeStamp):
    minutes = timeStamp // 60
    seconds = timeStamp % 60
    
    return str(minutes) + ":" + "{:02d}".format(int(seconds))

with open("albumList.txt") as albumList:
    youtube = youtubeuploader.get_authenticated_service()
    for album in albumList:
        formattedId = album.strip()
        try:
            archivedownloader.downloadAlbum(formattedId)
            tracksTimestamps = videocreator.createAlbumVideo(formattedId)
            youtubeuploader.uploadAlbum(youtube, formattedId, archivedownloader.getAlbumTitleAndCreator(formattedId), createVideoDescription(tracksTimestamps, formattedId))
            shutil.rmtree(formattedId, ignore_errors=True)
            os.remove(formattedId + ".mp4")
        except:
            print("Album " + formattedId + " Failed!")
            if Path(formattedId).is_dir():
                shutil.rmtree(formattedId, ignore_errors=True)
            ##if Path(formattedId + ".mp4").is_file():
                ##os.remove(formattedId + ".mp4")

