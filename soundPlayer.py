from threading import Thread
from playsound import playsound

def playAudio(path):
    soundThread = Thread(target = playsound,args=(path,))
    soundThread.start()

