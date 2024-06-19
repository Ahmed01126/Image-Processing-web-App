from flask import Flask, render_template, request
from combination import *
import base64
import os
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("temp.html")


def save_Image_In_The_Path(img, path):
    with open(path, 'wb') as pa:
        pa.write(img)


@app.route('/saveImg', methods=['POST', "GET"])
def save_Image():
    if request.method == "POST":
        list_img = os.listdir("static/images/output")
        for image in list_img:
            dir = "static/images/output/" + image
            os.remove(dir)
        save_Image_In_The_Path(base64.b64decode(request.form["original_1"].split(
            ',')[1]), './static/images/input/Image1.png')
        save_Image_In_The_Path(base64.b64decode(request.form["original_2"].split(
            ',')[1]), './static/images/input/Image2.png')
        ch = request.form["ch"]
        y11 = request.form["y11"]
        y21 = request.form["y21"]
        x11 = request.form["x11"]
        x21 = request.form["x21"]
        x12 = request.form["x12"]
        x22 = request.form["x22"]
        y12 = request.form["y12"]
        y22 = (request.form["y22"])
        cb_ph = request.form["cb_ph"]
        cb_amp = request.form["checkbox_Magnitude"]
        image1_ed = ((y11, y21), (x11, x21))
        image2_ed = ((y12, y22), (x12, x22))
        mixedImage = ImageCombination.Mixing(ch, image1_ed, image2_ed,
                                             cb_ph, cb_amp)
    return json.dumps({1: f'<img src="{mixedImage}"  id="comb_img" alt="" >'})


if __name__ == "__main__":
    app.run()
