import os
import sys
import json
import requests

env_translater_server = os.environ.get("TRANSLATER")
server = "http://" + env_translater_server

model_endpoint = {
    "headers": {'content-type': 'application/json'},
}



def STS(file_path,src_lang="en",target_lang="fr"):
    model_endpoint["url"] = str(server) + ":" + str(6000) + "translate_audio"
    request = {
        'file_path': file_path,
        "src_language": src_lang,
        "target_language": target_lang
    }
    res = requests.post(**model_endpoint, data=json.dumps(request), timeout=300)
    
    if res.status_code == 200:
        result = res.json()
        return result
    else:
        print("STS convertion failed")
        raise Exception("STS Convertion failed")

def STT(file_path,src_lang):
    model_endpoint["url"] = str(server) + ":" + str(6000) + "audio_to_text"
    request = {
        'file_path': file_path,
        "src_language": src_lang
    }
    res = requests.post(**model_endpoint, data=json.dumps(request), timeout=300)
    
    if res.status_code == 200:
        result = res.json()
        return result
    else:
        print("STT convertion failed")
        raise Exception("STT Conversion failed")


def TTT(file_path,src_lang,target_lang):
    model_endpoint["url"] = str(server) + ":" + str(6000) + "translate_text"
    request = {
        'file_path': file_path,
        "src_language": src_lang,
        "target_language": target_lang
    }
    res = requests.post(**model_endpoint, data=json.dumps(request), timeout=300)
    
    if res.status_code == 200:
        result = res.json()
        return result
    else:
        print("TTT convertion failed")

def TTS(file_path,src_lang,target_lang):
    model_endpoint["url"] = str(server) + ":" + str(6000) + "text_to_audio"
    request = {
        'file_path': file_path,
        "src_language": src_lang,
        "target_language": target_lang
    }
    res = requests.post(**model_endpoint, data=json.dumps(request), timeout=300)
    
    if res.status_code == 200:
        result = res.json()
        return result
    else:
        print("TTS convertion failed")