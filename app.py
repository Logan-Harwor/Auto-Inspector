import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def index():
    # just a form
    add_text = ""
    return render_template("index.html", add_text=add_text)

# ADD THESE ROUTES SO THE PWA WORKS:
@app.route('/manifest.json')
def serve_manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

@app.route('/sw.js')
def serve_sw():
    return send_from_directory(os.getcwd(), 'sw.js')

@app.route('/icon-192.png')
def serve_icon192():
    return send_from_directory(os.getcwd(), 'icon-192.png')

@app.route('/icon-512.png')
def serve_icon512():
    return send_from_directory(os.getcwd(), 'icon-512.png')

if __name__ == '__main__':
    app.run(debug=True)