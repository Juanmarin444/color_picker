from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    red_num = request.form['red']
    green_num = request.form['green']
    blue_num = request.form['blue']
    print(red_num, green_num, blue_num)

    return render_template('index.html', red=red_num, green=green_num, blue=blue_num)

app.run(debug=True)