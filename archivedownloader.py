from internetarchive import download, get_item
def downloadAlbum(id):
    download(identifier=id, verbose=True, checksum=True, glob_pattern="*.flac")
    download(identifier=id, verbose=True, checksum=True, glob_pattern="*cover*")
    download(identifier=id, verbose=True, checksum=True, glob_pattern="*folder*")

def getAlbumTitleAndCreator(id):
    metadata = get_item(id).metadata
    return metadata["title"] + " - " + metadata["creator"]