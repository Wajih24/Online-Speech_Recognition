import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])

install("SpeechRecognition")
install("pyttsx3")