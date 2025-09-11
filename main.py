from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    img_folder = "static/ela"
    photos = [
        f"{img_folder}/{file}" for file in os.listdir(img_folder)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]
    return render_template("index.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)