from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("test1.html", header="this is a test, my name is ryan")

@app.route("/<name>")
def name(name):
    return render_template("test1.html", header=name)

if __name__ == "__main__":
    app.run(debug=True)