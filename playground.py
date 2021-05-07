from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", amount = 3)

@app.route('/play/<x>')
def boxes(x):
    return render_template("index.html", amount = int(x))

@app.route('/play/<x>/<color>')
def colorBoxes(x, color):
    return render_template("index.html", amount = int(x), color =color)

if __name__=="__main__":  
    app.run(debug=True)