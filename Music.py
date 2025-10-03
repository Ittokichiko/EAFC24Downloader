import PyBass.bass as bass
from os import _exit as exit
def PlayMusic(filename : str):
    encoded_utf8 = filename.encode("utf-8")
    if(bass.BASS_INIT(device=-1, freq=44800, flags=0, win=0, dsguid=0)):
        bass.BASS_START()
        stream_music = bass.BASS_StreamCreateFile(mem=0, filename=encoded_utf8, offset=0, length=0, flags=0x4)
        bass.BASS_ChannelPlay(handle=stream_music, restart=False)
    else:
        print("Failed To Init PyBass!!!")
        exit(334)