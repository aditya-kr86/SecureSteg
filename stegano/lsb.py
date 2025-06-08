# stegano/lsb.py
from PIL import Image


def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    msg = message + chr(0)  # Add null char as end signal
    binary_msg = ''.join([format(ord(c), '08b') for c in msg])
    data_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(encoded.getpixel((x, y)))
            for n in range(3):  # RGB
                if data_index < len(binary_msg):
                    pixel[n] = (pixel[n] & ~1) | int(binary_msg[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_msg):
                break
        if data_index >= len(binary_msg):
            break

    encoded.save(output_path)


def decode_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ''

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for n in range(3):  # RGB
                binary_data += str(pixel[n] & 1)

    message = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i + 8]
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        message += char
    return message
