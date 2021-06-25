### Repository information
In this repository we find the delivery of the seminar 2 of the Audio and Video Encoding Systems subject (video part). 

In order to use this script we need to add inside the project folder the video "Big Buck Bunny" in mp4 format and with the following name: BBB.mp4. 

We have 5 .py files and in each of them we find a detailed explanation on how to use them:

## **main.py**
This is the base script of the project. In it we find a menu that allows us to select what transformation we want to do to the video. 
Since the original one is too long and the operations would take too long, just after running the script we extract 10 seconds of this video, with which we will work.

<img src="https://drive.google.com/uc?export=view&id=1ltl0h7RTRVFn0AwSgNZF75YR6bDsbzP-" width="300">


## **ex1.py**
Through this script we perform the operation mentioned above. From the original video we switch to a 10-second video (we cut from minute 03:00 to 03:10).
Below we can see the information of the original video and the trimmed video:

<img src="https://drive.google.com/uc?export=view&id=1eBCvUoY6ZAPgw-PTqd-Yz6j_YlnTWTG9" width="300"> <img src="https://drive.google.com/uc?export=view&id=1KI86MR_ZY0lEW-W-rp-K-DVSV_K4hOcI" width="300">

## **ex2.py**
We get the 10-second video with a real-time yuv format histogram superimposed. We can see an image of the result:

<img src="https://drive.google.com/uc?export=view&id=1Eu_u01Tzf4UbhwK6pykEe7CNDaO9JTm6" width="500">

## **ex3.py**
Running this script opens a menu with which we can choose the output resolution of the video. The output file may not correspond to the selected resolution since I have prioritized to preserve the aspect ratio, taking as reference the height of the video. In case you want to force the output resolution, an option would be:

`$ ffmpeg -i <input_file> -s 720x480 <output_file>`.

In our case, for the 160x120 option, for example, we have obtained: 

<img src="https://drive.google.com/uc?export=view&id=1YIpqjLvgLu6CtihJ3ITkBOWO_QLZW5cW" width="500">

## **ex4.py**
Finally, in this script we find a menu also with 2 options, which allows us to change the video audio from stereo to mono or change the audio codec to mp3: 

<img src="https://drive.google.com/uc?export=view&id=1Ztn907F-P-QLIx77_IlKkRSm4iKog_XA" width="300">

The results obtained after performing both are as follows:

<img src="https://drive.google.com/uc?export=view&id=1jkX0bPJXtiyzQoz3Rj66pah-l6yBO60c" width="300"> <img src="https://drive.google.com/uc?export=view&id=1EYU_zEek_BNze-K5JNpvO7ztgl162_za" width="300">

Translated with www.DeepL.com/Translator (free version)
