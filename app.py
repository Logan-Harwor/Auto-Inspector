from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def index():
    # just a form
    add_text = ""
    return render_template("index.html", add_text=add_text)

if __name__ == '__main__':
    app.run(debug=True)