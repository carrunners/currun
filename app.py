import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc83989cdfdd894859fkdlfd83i489ffjdj99'
global current_user
current_user = ""

@app.route('/')
def index():
    global current_user

    if current_user == "":
        print("first")
        current_user = request.environ['REMOTE_ADDR']
    return render_template('joystick.html')


@app.route('/forward_start')
def forward_start():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print("forward start")
    return "nothing"


@app.route('/forward_stop')
def forward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print("forward stop")
    return "nothing"


@app.route('/left_start')
def left_start():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:   
        print ("left start")
    return "nothing"


@app.route('/left_stop')
def left_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("left stop")
    return "nothing"


@app.route('/right_start')
def right_start():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("right start")
    return "nothing"


@app.route('/right_stop')
def right_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("right stop")
    return "nothing"


@app.route('/backward_start')
def backward_start():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("backward start")
    return "nothing"


@app.route('/backward_stop')
def backward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("backward stop")
    return "nothing"



if __name__ == "__main__":
    app.run(debug=True)
