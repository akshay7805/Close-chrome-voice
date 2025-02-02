import os 
import platform
import speech_recognition as sr
import sounddevice as sd 
import soundfile as sf
#function close the chrome
def close_chrome():
    if platform.system()=="Darwin" or platform.system()=="linux": 
        os.system("killall 'Google chrome'|| killall google-chrome || killall chromium")
#function recording audio using sounddevice
def record_audio(filename,Duration,samplerate=16000):
    print("recording...")
    audio=sr.record(int(Duration*samplerate), samplerate=samplerate,channels=1,dtype='float32')
    sd.wait() #wait until the recording
    sf.write(filename,audio,samplerate)
    print("recording is finished")
#function of speech recognizing
def speech_recognition():
    recognizer=sr.Recognizer()
    filename="siri 2.0"
    Duration=5
    record_audio(filename,Duration)
    with sr.AudioFile(filename) as source:
        try:
            audio=recognizer.record(source)
            command=recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")   
            if "close chrome" in command:
                close_chrome()
        except sr.UnknownValueError:
            print("Not understand the audio")
#call the function to start speech recognization            
speech_recognition()                     
