# app.py
from flask import Flask, render_template, request, send_file
import os
from stegano.lsb import encode_lsb, decode_lsb
from stegano.xor import xor_encrypt, xor_decrypt


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/text-in-image')
def text_in_image():
    return render_template('text-in-image.html')


@app.route('/image-in-image')
def image_in_image():
    return "<h2 style='text-align:center; margin-top:100px;'>🖼️ Feature Coming Soon in Version 2!</h2>"



@app.route('/encode', methods=['POST'])
def encode_route():
    file = request.files['image']
    message = request.form['message']
    key = request.form['key']


    image_path = 'static/input.png'
    output_path = 'static/encoded_image.png'

    file.save(image_path)
    encrypted_message = xor_encrypt(message, key)
    encode_lsb(image_path, encrypted_message, output_path)

    return render_template('result.html', encoded_image='encoded_image.png')




@app.route('/decode', methods=['POST'])
def decode():
    key = request.form['key']
    uploaded_file = request.files['encoded_image']
    input_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(input_path)

    decoded_encrypted = decode_lsb(input_path)
    message = xor_decrypt(decoded_encrypted, key)
    return render_template('result.html', decoded_message=message)


@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
