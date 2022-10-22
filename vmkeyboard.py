from pynput.keyboard import Listener as keyPressListener
from json import load
from soundPlayer import playAudio

class vmKeyboard:
    def __init__(this, key2soundPath) -> None:
        this.key2soundPath = key2soundPath
        this.defaultSoundPath = this.key2soundPath.get('default')
        

    def handleKeyPress(this,key):
        keyCapture = str(key)
        this.playKey(keyCapture)

    def playKey(this, key):
        soundPath = this.key2soundPath.get(key,this.defaultSoundPath)
        playAudio(soundPath)

if __name__ == '__main__':
    key2soundPathsList = load(open('./config.json')).get('soundFilePaths')
    key2soundPath = dict()
    for key2soundPathdict in key2soundPathsList:
        for key,value in key2soundPathdict.items():
            print(key,value)
            key2soundPath[key] = value

    vmSoundSimulator = vmKeyboard(key2soundPath)

    with keyPressListener(on_press=vmSoundSimulator.handleKeyPress,on_release=None) as listener:
        listener.join()