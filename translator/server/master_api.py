import os
import sys
import json
import traceback
from urllib import response

from redis import Redis
import cherrypy
import rq

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)


from pipeline.engine import audio_to_text_by_path as run_stt
from pipeline.engine import text_to_audio as run_tts
from pipeline.engine import audio_translator_by_path as run_sts
from pipeline.engine import text_translate as run_ttt
from utils.utils import load_json_file


config = load_json_file(os.path.join(ROOT_DIR,"config/config.json"))

env_redis_host = os.environ.get('REDIS_HOST')
if env_redis_host is not None:
    config['REDIS']['HOST'] = os.environ.get('REDIS_HOST')

class AudioDubAPI:
    def __init__(self,redis_host,redis_port):
        redis_conn = Redis(host=redis_host, port=redis_port)
        global queue_audio_to_text
        global queue_text_to_text
        global queue_text_to_audio
        global queue_audio_to_audio
        

        queue_audio_to_text = rq.Queue(name="at_queue", default_timeout='60m', connection=redis_conn)
        queue_text_to_text = rq.Queue(name="tt_queue", default_timeout='60m', connection=redis_conn)
        queue_text_to_audio = rq.Queue(name="ta_queue", default_timeout='60m', connection=redis_conn)
        queue_text_to_audio = rq.Queue(name="aa_queue", default_timeout='60m', connection=redis_conn)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def audio_to_text(self):
        response = {}
        try:
            request = cherrypy.request.json
            file_path = request["file_path"]
            language = request["src_language"]

            job = queue_audio_to_text.enqueue(run_stt,args=(file_path,language),job_timeout=3000, result_ttl=2400)

            job_id = job.get_id()
            while True:
                    if job:
                        if job.result is not None:
                            if 'error' in job.result:
                                response['error'] = job.result['error']
                            elif job.get_status() == 'failed':
                                response['error'] =  job.exc_info
                            elif job.get_status() == 'finished':
                                response.update(job.result)
                            break
                    else:
                        response['error'] = "job_not_found"
                        break
                    job = queue_audio_to_text.fetch_job(job_id)
        except Exception as e:
            response = {
                "error" : "invalid_request",
                "description": traceback.format_exc()
            }

        return response

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def text_to_audio(self):
        response = {}
        try:
            request = cherrypy.request.json
            input_text = request["text"]
            src_language = request["src_language"]
            target_language = request["target_language"]

            job = queue_audio_to_text.enqueue(run_tts,args=(input_text,src_language,target_language),job_timeout=3000, result_ttl=2400)

            job_id = job.get_id()
            while True:
                    if job:
                        if job.result is not None:
                            if 'error' in job.result:
                                response['error'] = job.result['error']
                            elif job.get_status() == 'failed':
                                response['error'] =  job.exc_info
                            elif job.get_status() == 'finished':
                                response.update(job.result)
                            break
                    else:
                        response['error'] = "job_not_found"
                        break
                    job = queue_audio_to_text.fetch_job(job_id)
        except Exception as e:
            response = {
                "error" : "invalid_request",
                "description": traceback.format_exc()
            }
        return response

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def translate_audio(self):
        response = {}
        try:
            request = cherrypy.request.json
            file_path = request["file_path"]
            src_language = request["src_language"]
            target_language = request["target_language"]

            job = queue_audio_to_audio.enqueue(run_sts,args=(file_path,src_language,target_language),job_timeout=3000, result_ttl=2400)

            job_id = job.get_id()
            while True:
                    if job:
                        if job.result is not None:
                            if 'error' in job.result:
                                response['error'] = job.result['error']
                            elif job.get_status() == 'failed':
                                response['error'] =  job.exc_info
                            elif job.get_status() == 'finished':
                                response.update(job.result)
                            break
                    else:
                        response['error'] = "job_not_found"
                        break
                    job = queue_audio_to_text.fetch_job(job_id)
        except Exception as e:
            response = {
                "error" : "invalid_request",
                "description": traceback.format_exc()
            }
        return response

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def translate_text(self):
        response = {}
        try:
            request = cherrypy.request.json
            input_text = request["text"]
            src_language = request["src_language"]
            target_language = request["target_language"]

            job = queue_audio_to_text.enqueue(run_ttt,args=(input_text,src_language,target_language),job_timeout=3000, result_ttl=2400)

            job_id = job.get_id()
            while True:
                    if job:
                        if job.result is not None:
                            if 'error' in job.result:
                                response['error'] = job.result['error']
                            elif job.get_status() == 'failed':
                                response['error'] =  job.exc_info
                            elif job.get_status() == 'finished':
                                response.update(job.result)
                            break
                    else:
                        response['error'] = "job_not_found"
                        break
                    job = queue_audio_to_text.fetch_job(job_id)
        except Exception as e:
            response = {
                "error" : "invalid_request",
                "description": traceback.format_exc()
            }
        return response

def main():
    api = AudioDubAPI(config['REDIS']['HOST'], config['REDIS']['PORT'])
    cherrypy.tree.mount(api.audio_to_text, '/audio_to_text/', {})
    cherrypy.tree.mount(api.text_to_audio, '/text_to_audio/', {})
    cherrypy.tree.mount(api.translate_audio, '/translate_audio/', {})
    cherrypy.tree.mount(api.translate_text, "/translate_text")

    cherrypy.config.update(config['REST_SERVER'])
    cherrypy.engine.signals.subscribe()
    cherrypy.quickstart(script_name='/', root=None)


if __name__ == "__main__":
    main()
    print("API has started")




        
