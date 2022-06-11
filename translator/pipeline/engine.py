import os
import sys
import json
import traceback

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
env_redis_host = os.environ.get("REDIS_HOST")
env_src_mnt_vol = os.environ.get("SRC_MOUNT_VOLUME")
env_dest_mnt_vol = os.environ.get("DEST_MOUNT_VOLUME")

from utils.utils import convert_audio_to_text
from transformers import AutoTokenizer,TFAutoModelForSequenceClassification,pipeline


def audio_translator_by_path(file_path,src_lang="en",target_lang=None):
    if file_path is not None and os.path.exists(file_path):
        result = convert_audio_to_text(file_path)
        if "error" in result:
            return result
        else:
            translated_text = text_translate(result["text"],target_lang="fr")
            return result
    else:
        result = {
            "error": "file_not_found",
            "description": "file_not_found"
        }

def audio_to_text_by_path(file_path,src_lang="en",target_lang='en'):
    if file_path is not None :
        result = convert_audio_to_text(file_path)
        return result
    else:
        result = {
            "error": "file_not_found",
            "description": "file_not_found"
        }


def text_translate(text,src_lang="en",target_lang="fr"):
    try:
        if src_lang == "en" and target_lang == "fr":
            model_checkpoint = "Helsinki-NLP/opus-mt-en-fr"
            translator = pipeline("translation", model=model_checkpoint)
            translated_text = translator(str(text).strip())
            translated_text = translated_text[0]["translation_text"]
            result = {
                "text": translated_text
            }
        else:
            result = {
                "error": "language translation model is not found this combination",
                "description": "language translation combination is not found"
            }
    except Exception as e:
        print(traceback.print_exc())
        result = {
            "error":  "error occured while translating text",
            "description": traceback.format_exc()
        }
    return result

def text_to_audio(input_text,src_lang="fr",target_lang="fr"):
    try:
        if src_lang == "fr" and target_lang == "fr":
            pass
        else:
            result = {
                    "error": "language translation model is not found this combination",
                    "description": "language translation combination is not found"
                }
    except Exception as e:
        print(traceback.print_exc())
        result = {
            "error":  "error occured while translating text",
            "description": traceback.format_exc()
        }
    return result


if __name__ = "__main__":
    