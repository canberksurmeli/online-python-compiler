from flask import Flask, request, render_template, send_file, jsonify
from os import remove
from glob import glob


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/generate', methods=["POST"])
def response():
    try:
        data = request.get_json().get("code")
        print(data)
        exec(data)

        png_name = glob("*.png")[0]

        file = send_file(png_name, mimetype='image/png')
        remove(png_name)
        return file
    except Exception as e:
        print(e)
        png_list = glob("*.png")
        if len(png_list) > 0:
            remove(png_list[0])
        return jsonify(
            msg="Hatalı bir input girdiniz. Lütfen tekrar deneyiniz.",
            err= str(e)
        ), 467


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
