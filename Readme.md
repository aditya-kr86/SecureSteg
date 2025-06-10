# SecureSteg - Text-in-Image Steganography Web App (V1)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

SecureSteg is a simple yet powerful Flask-based web application that allows users to **encode secret text messages into PNG images** using **LSB (Least Significant Bit) steganography** combined with **XOR encryption** for added security. It also supports decoding the secret message from the encoded images.

This project aims to demonstrate practical steganography techniques with a focus on usability, security, and clean design.

---

## Features (V1)

- Encode a **text message** securely inside a PNG image
- Decode the secret message from an encoded PNG image
- XOR encryption using a **user-provided secret key** for extra security
- Basic validation on file types and message lengths
- User-friendly UI with encoding/decoding forms
- Download the encoded image safely
- Basic logging and error handling
- Clear instructions and alerts for user guidance

---

## Technology Stack

- **Python 3.8+**
- **Flask** — Lightweight web framework
- **Stegano** — Python library for LSB steganography
- **HTML/CSS + Bootstrap** — For responsive UI
- **JavaScript** — For form validations & UX enhancements

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/securesteg.git
   cd securesteg
    ````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   python app.py
   ```

5. **Open your browser** at `http://127.0.0.1:5000`

---

## Usage

* **Encode Message**
  Upload a PNG image, enter your secret message and a secret key, then encode it. Download the resulting encoded image.

* **Decode Message**
  Upload an encoded PNG image and enter the secret key used during encoding to retrieve the hidden message.

---

## Important Notes

* Only **PNG** images are supported for encoding and decoding.
* The secret key is used for XOR encryption, so the same key must be used for encoding and decoding.
* Avoid sharing encoded images through apps like WhatsApp that compress images, as this may corrupt the hidden message.
* Limit your secret message length to ensure smooth encoding.

---

## Folder Structure

```
securesteg/
├── app.py
├── xor.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── text-in-image.html
│   └── result.html
├── static/
│   ├── css/
│   └── images/
├── uploads/
└── output/
```

---

## Future Scope (Upcoming Versions)

* Encode **image inside image** steganography
* Support for more image formats (JPEG, BMP)
* User authentication & saved history
* Enhanced UI with drag-and-drop & progress bars
* Advanced encryption options (AES, RSA)
* Real-time encoding/decoding progress monitoring
* Deployment on cloud platforms (Heroku, AWS)

---

## Contributors

* **Aditya Kumar** - Developer & Project Lead
  *Azure Data Scientist Associate | Python & Flask Enthusiast*

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or collaboration, reach out at:
**Website:** [adityakr.me](https://adityakr.me)
**Email:** [aditya_kumar_gupta@yahoo.com](mailto:aditya_kumar_gupta@yahoo.com)
**GitHub:** [github.com/aditya-kr86](https://github.com/aditya-kr86)
**LinkedIn:** [linkedin.com/in/aditya-kr86](https://linkedin.com/in/adityakr-86)

---

Thank you for checking out SecureSteg!
Stay tuned for exciting updates. 🚀

