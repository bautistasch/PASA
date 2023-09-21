import subprocess
import os
from pytube import YouTube

def get_wav_from_youtube(video_url = 'https://www.youtube.com/watch?v=GvLc5r6HBUU', time_interval_ms = (1000, 2000), output_title = None):

    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()


    stream.download(filename=f'{yt.title}.mp4')

    # Ahora paso el mp4 a wav con FFmpeg
    ffmpeg_path = r'D:\ffmpeg\bin\ffmpeg.exe'

    input_video = f'{yt.title}.mp4'

    output_wav = f'{yt.title}_SONG.wav'

    command = [
        ffmpeg_path,
        '-i', input_video,
        '-acodec', 'pcm_s16le',  # PCM
        '-ar', '48000',          # 48k
        '-ac', '1',              # Mono
        output_wav
    ]

    subprocess.run(command)

    from pydub import AudioSegment
    song = AudioSegment.from_wav(output_wav)
    sliced_audio = song[time_interval_ms[0]:time_interval_ms[1]]
    if output_title != None:
        output_wav = output_title
    sliced_audio.export(output_wav, format="wav")



#get_wav_from_youtube(video_url = 'https://www.youtube.com/watch?v=GvLc5r6HBUU', time_interval_ms = (34000, 44000), output_title = 'musica_raw.wav')
#get_wav_from_youtube(video_url = 'https://youtu.be/XbPHojL_61U', time_interval_ms = (68*60*1000+1000*48, 68*60*1000+1000*48 + 1000*10), output_title = 'people_talking_raw.wav')



