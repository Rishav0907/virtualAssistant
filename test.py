import speech_recognition as sr
import os
import subprocess
import pyfiglet
from termcolor import colored
from gtts import gTTS
import time

tts=gTTS(text="Hello I am back to your service sir",lang='en-us')
tts.save("Initial.mp3")
os.system("mpg321 Initial.mp3 -quiet")
print("First pull request")
def listenToMe():
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            subprocess.call('clear')
            banner=pyfiglet.figlet_format('Virtual Assistant')
            color=colored(banner,color='red')
            print(color)
            print("Give your command sir")
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)

            try:
                command=r.recognize_google(audio)
                print(command)
                if 'Google' in command:
                    print("Opening google")
                    tts2=gTTS(text="Opening Google Chrome sir",lang='en-us')
                    tts2.save("command.mp3")
                    os.system("mpg123 command.mp3")
                    os.system('google-chrome')
                if 'media' in command:
                    print("opeing vlc media player")
                    tts4=gTTS(text="Opening VLC media player sir",lang='en-us')
                    tts4.save('command.mp3')
                    os.system('mpg123 command.mp3')
                    os.system('vlc')
                if 'Visual' in command:
                    print("opening visual studio code")
                    tts5=gTTS(text="Opening visual studio code sir",lang='en-us')
                    tts5.save('command.mp3')
                    os.system('mpg123 command.mp3')
                    os.system('code')
                if 'Jarvis' in command:
                    tts3=gTTS(text='Hello Sir',lang='en-us')
                    tts3.save('command.mp3')
                    os.system('mpg123 command.mp3')
                else:
                    ttsf=gTTS(text="Sorry I cannot perform this task sir",lang='en-us')
                    ttsf.save('command.mp3')
                    os.system('mpg123 command.mp3')
            except sr.UnknownValueError as msg:
                print(msg)
                listenToMe()


listenToMe()
