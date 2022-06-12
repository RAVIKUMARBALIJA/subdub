import os
import traceback
import speech_recognition as speech_rec
import json
from gtts import gTTS  
from playsound import playsound  

def convert_audio_to_text(file_path):
    recogniser = speech_rec.Recognizer()

    try:
        with speech_rec.AudioFile(str(file_path)) as source:
            audio_data = recogniser.record(source)
            print(audio_data)
            # recognize (convert from speech to text)
            text = recogniser.recognize_google(audio_data)
            result = {
                "text": text
            }
    except Exception as e:
        traceback.format_exc()
        result = {
            "error" : e,
            "description":  traceback.format_exc(e)
        }
    
    return result


def load_json_file(file_path):
    with open(file_path,"r") as f:
        return json.load(f)


def text_to_speech(text,file_path,target_lang="fr",):    
    try:
        obj = gTTS(text=text, lang=target_lang, slow=False) 
        obj.save(str(file_path))
    except Exception as e:
        result = {
            "error": "text to speech convertion failed",
            "desrption": traceback.format_exc()
        }  

if __name__ == "__main__":
    result = convert_audio_to_text("/home/ravikumar/Downloads/123.wav")
    print(result)
