# -*- coding: utf-8 -*-
'''
Ref:
    https://www.sololinux.es/manual-de-ffmpeg-con-ejemplos-parte-1-de-2/#Recortar_archivos_de_audio_y_video
'''

import subprocess

subprocess.call('ffmpeg -i BBB.mp4 -ss 00:03:00 -to 00:03:10 BBB10.mp4', shell=True)
