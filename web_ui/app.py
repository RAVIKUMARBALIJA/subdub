from flask import Flask,render_template,request
import speech_recognition as sr 
from werkzeug.utils import secure_filename
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
r = sr.Recognizer()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/check_audio', methods = ['GET', 'POST'])
# def check_audio():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return 'file uploaded successfully'

    
#     return "Failed"
#     # sound = AudioSegment.from_wav(path)
#     # chunks = split_on_silence(sound,
#     #     min_silence_len = 500,
#     #     silence_thresh = sound.dBFS-14,
#     #     keep_silence=500,
#     # )
#     # folder_name = "audio-chunks"
#     # if not os.path.isdir(folder_name):
#     #     os.mkdir(folder_name)
#     # whole_text = ""
#     # for i, audio_chunk in enumerate(chunks, start=1):
#     #     chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#     #     audio_chunk.export(chunk_filename, format="wav")
#     #     with sr.AudioFile(chunk_filename) as source:
#     #         audio_listened = r.record(source)
#     #         try:
#     #             text = r.recognize_google(audio_listened)
#     #         except sr.UnknownValueError as e:
#     #             print("Error:", str(e))
#     #         else:
#     #             text = f"{text.capitalize()}. "
#     #             print(chunk_filename, ":", text)
#     #             whole_text += text
#     # return whole_text


if "__main__"== __name__:
    app.run(debug=True)