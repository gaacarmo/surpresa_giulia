from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/ela"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    img_folder = "static/ela"
    photos = [
        f"ela/{file}" for file in os.listdir(img_folder)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]
    return render_template("index.html", photos=photos)

@app.route("/upload", methods=["POST"])
def upload():
    if 'photo' not in request.files:
        return redirect(url_for('index'))
    file = request.files['photo']
    if file.filename == '':
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    return redirect(url_for('index'))