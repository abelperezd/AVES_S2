# -*- coding: utf-8 -*-
'''
Ref:
    https://trac.ffmpeg.org/wiki/Histogram
'''

import subprocess


subprocess.call('ffmpeg -i BBB10.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" BBB10hist.mp4', shell=True)
