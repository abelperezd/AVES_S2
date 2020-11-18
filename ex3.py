# -*- coding: utf-8 -*-
'''
Ref:
    https://trac.ffmpeg.org/wiki/Scaling
'''

import subprocess


def enunciado():
    print("Selecciona la resolución de salida: ")
    print("[1]: 720p")
    print("[2]: 480p")
    print("[3]: 360x240")
    print("[4]: 160x120")
    print("[any]: Return")
    x = input()
    return x


x = enunciado()

if x == 1:
    subprocess.call('ffmpeg -i BBB10.mp4 -vf scale=1280:-1 BBB10_720p.mp4', shell=True)
elif x == 2:
    subprocess.call('ffmpeg -i BBB10.mp4 -vf scale=720:480 BBB10_480p.mp4', shell=True)
elif x == 3:
    subprocess.call('ffmpeg -i BBB10.mp4 -vf scale=360:240 BBB10_360x240.mp4', shell=True)
elif x == 4:
    subprocess.call('ffmpeg -i BBB10.mp4 -vf scale=160:120 BBB10_160x120.mp4', shell=True)
else:
    print('Return')
