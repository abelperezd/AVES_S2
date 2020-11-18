# -*- coding: utf-8 -*-
'''
Este es el script principal. Una vez lo ejecutamos, recortamos el archivo BBB.mp4 y a partir
del vídeo recortado, comenzamos a trabajar.
'''

import os
import sys
import subprocess


def enunciado():
    print("\nIntroduce un número para realizar una de las siguientes operaciones:")
    print("\n[1]: Guardar un histograma en directo del vídeo")
    print("\n[2]: Cambiar resolución del vídeo")
    print("\n[3]: Cambiar el audio del vídeo a mono o a mp3")
    print("\n[0]: Exit")
    x = input()
    return x


os.system("python ex1.py")

print("Para este script se necesita el vídeo Big Buck Bunny con nombre y formato BBB.mp4 dentro de la carpeta.")
print("Si no dispones de el, presiona [0]")

while (True):
    x = enunciado()

    if x == 1:
        os.system("python ex2.py")
    elif x == 2:
        os.system("python ex3.py")
    elif x == 3:
        os.system("python ex4.py")
    elif x == 0:
        sys.exit()
    else:
        print('Introducir opción válida')
