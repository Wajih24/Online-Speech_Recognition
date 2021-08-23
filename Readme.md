# Online Speech_Recognition
 The first main project is an online speech_recognition using Google speech API , it's a free source that doesn't require any subscription fees. 

## Getting Started 
# Step 1 : package installation 
To make sure that everything will work fine , Python 3.6 or higher is required 
==> For Windows users : 
``` bash
#Our main packages 'SpeechRecognition' and 'pyttsx3'
pip install pyttsx3 SpeechRecognition 

#Also PyAudio is required for Microphone users 
pip install pyaudio

# If an error ouccured while installing PyAudio 
==> you need to go to : "https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio"
==> Install the wheel according to your version : for example if you are using 3.8 python you should look for a version with 'cp38' in name and 64bit system you should look for 'win_amd64' if 32bit so it will be 'win32'
==> after you place the downloaded .whl file in your project folder and run this command :
pip install <.whl file_name> 
*In my case this will be the command :  
pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl 
*In case you placed the file on another folder you need to need to give the full path + file name :
pip install <file_path + .whl file_name> 
```

==> For Unbuntu users : 
``` bash
#Install 'SpeechRecognition '
sudo pip3 install SpeechRecognition  

#Install 'pyttsx3'
sudo pip3 install pyttsx3 

#We need to install Pyaudio but first we need to make sure that to install these dependencies
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
#Now ready to install 'PyAudio'
sudo pip3 install PyAudio

#And one more dependencie to get everything working fine 
sudo apt-get install espeak
``` 
### To mention if an error ouccured while installing "SpeechRecognition" while using the given command a setup.py will be attached with the folder , you just need to make sure that pip installed and working fine and run that file and "SpeechRecognition" will be installed 

# Step 2 : Running 
So now moving to the running process , things are similar between Windows and Unbuntu users :
1- cd <project_folder_path>
2- python main.py
3- a log.txt will be created that contains the text speech of each time 
