Flask Project
    
    This Flask application is a simple and efficient tool for generating QR codes from uploaded files. In this application, the user uploads a file,     encodes it into a base64 string, and embeds it in a URL. A QR code is then generated from this URL and can be downloaded and shared; when the QR     code is scanned, the URL opens and the embedded file can be downloaded.

Main Functions
    File uploading: Users can upload files in any format.
    QR Code generation: A QR Code is generated from the uploaded file.
    File Download: Allows users to download and share the generated QR Code.
    HTML Decoder

    HTML Decoder is a web page that decodes data embedded in a URL, downloads the decoded data as a file, decodes the data from the URL using            JavaScript, creates a Blob from the decoded data, and downloads the Blob link. When the page is opened, the download link is automatically           clicked and the file is downloaded.

Data decoding: The decoder can decode the data embedded in the URL.
File download: Decoded data is downloaded as a file.
Broad compatibility: The decoder works with any file that can be encoded into a base64 string.

These projects are for educational purposes only and should not be used in a production environment without further modifications for security       and efficiency. Please let us know if you have any questions or requests.


Requirements:
    apt install python3-flask
    apt install python3-pip
    pip3 install pypng
    pip3 install qrcode


Usage:
    export FLASK_APP=app.py
    flask run
