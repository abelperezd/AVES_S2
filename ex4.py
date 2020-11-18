# -*- coding: utf-8 -*-
'''
Ref:
    https://trac.ffmpeg.org/wiki/AudioChannelManipulation
'''

import subprocess


def enunciado():
    print("Selecciona una opción: ")
    print("[1]: Pasar a audio Mono")
    print("[2]: Cambiar codec de audio a mp3")
    print("[any]: Return")
    x = input()
    return x


x = enunciado()

if x == 1:
    subprocess.call('ffmpeg -i BBB10.mp4 -ac 1 BBB10_audio_mono.mp4', shell=True)
elif x == 2:
    subprocess.call('ffmpeg -i BBB10.mp4 -c:a mp3 BBB10_audio_mp3.mp4', shell=True)
else:
    print('Return')
