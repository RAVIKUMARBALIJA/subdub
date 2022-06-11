import os
import traceback
import speech_recognition as speech_rec
import json

def convert_audio_to_text(file_path):
    recogniser = speech_rec.Recogniser()

    try:
        with speech_rec.AudioFile(file_path) as source:
            audio_data = recogniser.record(source)
            # recognize (convert from speech to text)
            text = recogniser.recognize_google(audio_data)
            result = {
                "text": text
            }
    except Exception as e:
        traceback.format_exception(e)
        result = {
            "error" : e.args[0],
            "description":  e.args[1]
        }
    
    return result

def load_json_file(file_path):
    with open(file_path,"r") as f:
        return json.load(f)

