import archivedownloader
import videocreator

with open("albumList.txt") as albumList:
    for album in albumList:
        archivedownloader.downloadAlbum(album)
        videocreator.createAlbumVideo(album)