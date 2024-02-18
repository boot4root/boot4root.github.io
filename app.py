from flask import Flask, render_template, request, send_file
import os
import base64
import qrcode
import urllib.parse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(file.filename)
            with open(file.filename, "rb") as f_obj:
                f_contents = f_obj.read()
            enc_contents = base64.b64encode(f_contents).decode('ascii')
            url_enc_contents = urllib.parse.quote_plus(enc_contents)
            full_link = f"https://boot4root.github.io/decode.html?f={file.filename}#{url_enc_contents}"
            qr_code_img = qrcode.make(full_link)
            qr_code_img.save(f"{file.filename}_qr.png")
            return send_file(f"{file.filename}_qr.png", as_attachment=True)
    return '''
    <!doctype html>
    <title>Upload Image</title>
    <h1>Upload Image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
