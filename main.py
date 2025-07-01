import archivedownloader
import videocreator
import youtubeuploader
import os
import shutil

with open("albumList.txt") as albumList:
    youtube = youtubeuploader.get_authenticated_service()
    for album in albumList:
        formattedId = album.strip()
        archivedownloader.downloadAlbum(formattedId)
        videocreator.createAlbumVideo(formattedId)
        youtubeuploader.uploadAlbum(youtube, formattedId, archivedownloader.getAlbumTitleAndCreator(formattedId))
        shutil.rmtree(formattedId, ignore_errors=True)
        os.remove(formattedId + ".mp4")