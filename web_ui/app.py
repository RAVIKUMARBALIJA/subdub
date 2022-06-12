from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os 

from utils import STS,STS,TTS,TTT

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/translate_audio', methods = ['POST'])
def translate_audio():
    f = request.files['files']
    if request.method == 'POST':
        filename = "final"+".wav"
        p = os.path.join("uploads",filename)
        f.save(p)
        result = STS(p,"en","fr")
        return result


