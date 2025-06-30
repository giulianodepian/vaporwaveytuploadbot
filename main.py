import archivedownloader
import videocreator
import youtubeuploader

with open("albumList.txt") as albumList:
    youtube = youtubeuploader.get_authenticated_service()
    for album in albumList:
        archivedownloader.downloadAlbum(album)
        videocreator.createAlbumVideo(album)
        youtubeuploader.uploadAlbum(youtube, album)