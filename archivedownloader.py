from internetarchive import download
def downloadAlbum(id):
    download(identifier=id, verbose=True, checksum=True, glob_pattern="*.flac")
    download(identifier=id, verbose=True, checksum=True, glob_pattern="*cover_itemimage*")