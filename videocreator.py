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

def createAlbumVideo(id):
    p = Path(id)

    tracks = []
    for audio in p.glob("*.flac"):
        tracks.append(AudioFileClip(audio))
    finalTrack = concatenate_audioclips(tracks)
    finalVideo = ImageClip("./" + id + "/cover_itemimage.jpg", duration=finalTrack.duration)
    finalVideo = finalVideo.with_audio(finalTrack)
    finalVideo.write_videofile(id + ".mp4", fps=30)
    
    