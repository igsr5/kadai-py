import os
import numby as np
import cv2
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "./upload"
IMG_WIDTH = 320
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html", title="flask test", name = name)

@app.route('/send', methods=["POST"])

def send():
    img_file = request.files["img_file"]
    filename = secure_filename(img_file.filename)
    p_fname = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    img_file.save(p_fname)
    img = cv2.resize(img, (IMG_WIDTH), int(IMG_WIDTH * img.shope[0] / img.shope[1]))

    raw_img_url = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)

    after_img_url = os.path.join(app.config["UPLOAD_FOLDER"], "after_"+filename)
    
    cv2.imwrite(after_img_url, after_img)

    return render_template("index.html", title = "After ...", raw_img_url = raw_img_url, after_img_url = after_img_url)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
