import archivedownloader
import videocreator
import youtubeuploader
import os
import shutil

with open("albumList.txt") as albumList:
    youtube = youtubeuploader.get_authenticated_service()
    for album in albumList:
        formattedAlbum = album.strip()
        archivedownloader.downloadAlbum(formattedAlbum)
        videocreator.createAlbumVideo(formattedAlbum)
        youtubeuploader.uploadAlbum(youtube, formattedAlbum)
        shutil.rmtree(formattedAlbum, ignore_errors=True)
        os.remove(formattedAlbum + ".mp4")