from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os 
import time

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")


@app.route('/final_result')
def final_result():
    filename = "hello.wav"
    return render_template("final_result.html",filenames = filename)


@app.route('/record')
def record():

    return render_template("record.html")

@app.route('/save_recording',methods=["POST"])
def save_reco():
    if request.method == "POST":
        f = open('./file1.wav', 'wb')
        f.write(request.get_data("audio_data"))
        # ts = int(time.time())
        # filename = "recording"+wav
        f.close()
        
        return render_template("index.html")

    route('/')


@app.route("/translate_audio", methods=["POST"])
def check_audio():
    file = request.files['files']

    # file.save(f'uploads/{file.filename}')
            
    filename = "final"+'.wav'
    p = os.path.join('uploads/', filename)
    file.save(p)
    return "Successful"
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
    app.run(debug = True)