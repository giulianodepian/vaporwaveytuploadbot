from moviepy import (
    ImageClip,
    AudioClip,
    AudioFileClip,
    CompositeAudioClip,
    VideoClip,
    ImageClip,
    concatenate_audioclips
)
from pathlib import Path
import glob

def createAlbumVideo(id, listOfTracks):
    p = Path(id)
    tracks = []
    tracksTimeStamps = []
    totalTimeInSeconds = 0
    for track in listOfTracks:
        tracks.append(AudioFileClip(list(p.glob("*" + glob.escape(track) + ".flac"))[0]))
    ##for audio in p.glob("*.flac"):
    ##    tracks.append(AudioFileClip(audio))
    finalTrack = concatenate_audioclips(tracks)
    for track in tracks:
        tracksTimeStamps.append(int(totalTimeInSeconds))
        totalTimeInSeconds += track.duration
    images = list(p.glob("*cover*.*"))
    finalVideo = ImageClip(images[0], duration=finalTrack.duration)
    finalVideo = finalVideo.with_audio(finalTrack)
    finalVideo.write_videofile(id + ".mp4", fps=24, logger=None, threads=8, preset="superfast")
    finalVideo.close()

    return tracksTimeStamps
    
    