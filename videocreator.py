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
    existVideo = Path(id + ".mp4").is_file()
    
    if existVideo == False:
        p = Path(id)

        tracks = []
        for audio in p.glob("*.flac"):
            tracks.append(AudioFileClip(audio))
        finalTrack = concatenate_audioclips(tracks)
        for image in p.glob("*cover_itemimage*"):
            finalVideo = ImageClip(image, duration=finalTrack.duration)
        finalVideo = finalVideo.with_audio(finalTrack)
        finalVideo.write_videofile(id + ".mp4", fps=30)
    else:
        print("Video Already Exist")
    
    