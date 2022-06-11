import os
import sys
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
env_redis_host = os.environ.get("REDIS_HOST")


import speech_recognition as speech_rec


def audio_translator_path(file_path,src_lang=None,target_lang=None):



def audio_to_text_by_path(file_path,src_lang=None,target_lang='en'):




def text_to_audio(text,target_lang=None):