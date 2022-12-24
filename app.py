from flask import Flask, render_template, request
import OPi.GPIO as GPIO

#IN1 - purple - forward, IN2 - green - backward, ENB - blue - speed, servo - orange - rotation
forward_pin = 3 #PA12
backward_pin = 5 #PA11
speed_pin = 7 #PA6
servo_pin = 11 #PA1
dc = 30
hz = 25
pwm = GPIO.PWM(speed_pin, hz)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(forward_pin, GPIO.OUT)
GPIO.setup(backward_pin, GPIO.OUT)
GPIO.setup(speed_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)
#GPIO.output(forward_pin, 1)

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
        #pwm.start(dc)
    return "nothing"


@app.route('/forward_stop')
def forward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print("forward stop")
        GPIO.output(forward_pin, 0)
        GPIO.output(backward_pin, 0)
        #pwm.stop()
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
        GPIO.output(backward_pin, 1)
        #pwm.start(dc)
    return "nothing"


@app.route('/backward_stop')
def backward_stop():
    global current_user
    if current_user == request.environ['REMOTE_ADDR']:
        print ("backward stop")
        GPIO.output(forward_pin, 0)
        GPIO.output(backward_pin, 0)
        #pwm.stop()
    return "nothing"

@app.route('/exit')
def exit():
    global current_user
    current_user = ""
    print("exit")
    return "nothing"


if __name__ == "__main__":
    app.run(debug=True)
