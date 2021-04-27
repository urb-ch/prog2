from flask import Flask
from flask import render_template

app = Flask("Hello")

@app.route("/hello/")
@app.route('/hello/<name>')
def hello(name=False):
    if name:
        return render_template('hello.html', name=name)
    else:
        return "Not Hallo World again.."

@app.route("/test")
def test():
    return "success"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
