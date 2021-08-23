import speech_recognition as sr
import pyttsx3
from datetime import datetime
from datetime import date
today = date.today()
day = today.strftime("%b-%d-%Y")
with open("log"+day+".txt", 'a') as f:
    print('File created for this day : ', day)
    f.close()
    
def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()

def speech_to_text():
    required=-1
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required= index
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=4)
    try:
        input = r.recognize_google(audio)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string);print("You said: " + input)
        text = dt_string + ": " + input +"\n"
        with open("log"+day+".txt", 'a') as f:
            f.write(text)
            f.close()
        #speak("You said: " + input +".")
        return str(input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
while(True):
    speech_to_text()