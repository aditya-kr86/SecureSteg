# app.py
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
from stegano.lsb import encode_lsb, decode_lsb
from stegano.xor import xor_encrypt, xor_decrypt
import logging
import uuid
import threading
import time
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # required for flashing messages
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Helper function to delete a file after delay
def delete_file_later(path, delay=30):
    def delete():
        try:
            if os.path.exists(path):
                os.remove(path)
                logging.info(f"Deleted file: {path}")
        except Exception as e:
            logging.error(f"Error deleting file {path}: {e}")
    timer = threading.Timer(delay, delete)
    timer.daemon = True
    timer.start()


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
    if len(message) > 1000:
        flash("⚠️ Message too long. Please limit to 1000 characters.", "warning")
        return redirect(url_for('text_in_image'))

    # Generate unique filenames
    unique_id = str(uuid.uuid4())
    image_path = os.path.join(UPLOAD_FOLDER, f"input_{unique_id}.png")
    output_filename = f"encoded_{unique_id}.png"
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    file.save(image_path)
    encrypted_message = xor_encrypt(message, key)
    encode_lsb(image_path, encrypted_message, output_path)
    logging.info("Image encoded successfully.")

    # Schedule deletion of the encoded image after 5 minutes
    delete_file_later(output_path, delay=30)
    # Optionally, also delete the uploaded input image after a short delay
    delete_file_later(image_path, delay=30)

    return render_template('result.html', encoded_image=output_filename)

@app.route('/decode', methods=['POST'])
def decode():
    key = request.form['key']
    uploaded_file = request.files['encoded_image']
    unique_id = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_FOLDER, f"input_{unique_id}.png")
    uploaded_file.save(input_path)

    decoded_encrypted = decode_lsb(input_path)
    message = xor_decrypt(decoded_encrypted, key)
    logging.info("Image Decoded successfully.")
    delete_file_later(input_path, delay=30)
    return render_template('result.html', decoded_message=message)


@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
