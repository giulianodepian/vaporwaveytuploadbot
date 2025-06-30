import archivedownloader

with open("albumList.txt") as albumList:
    archivedownloader.downloadAlbum(albumList.readline())