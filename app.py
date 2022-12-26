from flask import Flask, render_template, request
import OPi.GPIO as GPIO
import requests
import time

forward_pin = 'PA1'#3 #PA12
backward_pin = 'PA0' #PA11

GPIO.setmode(GPIO.SUNXI)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)

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
        GPIO.output(forward_pin, 1)
        GPIO.output(backward_pin, 0)
    return "nothing"


@app.route('/forward_stop')
def forward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print("forward stop")
        GPIO.output(forward_pin, 0)
        GPIO.output(backward_pin, 0)	
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
        GPIO.output(forward_pin, 0)
        GPIO.output(backward_pin,1)
    return "nothing"


@app.route('/backward_stop')
def backward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("backward stop")
        GPIO.output(forward_pin, 0)
        GPIO.output(backward_pin, 0)
    return "nothing"

@app.route('/exit')
def exit():
    global current_user
    current_user = ""
    print("exit")
    return "nothing"


if __name__ == "__main__":
	while True:
		try:
			requests.get('https://www.google.com/').status_code
			break
		except:
			time.sleep(2)
			pass
	app.run(host='192.168.10.157', port=5000, debug=True)