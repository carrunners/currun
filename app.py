from flask import Flask, render_template, request

@app.route('/')
def index():
    return render_template('joystick.html')


@app.route('/forward_start')
def forward_start():
    print("forward start")
    return "nothing"


@app.route('/forward_stop')
def forward_stop():
    print("forward stop")
    return "nothing"


@app.route('/left_start')
def left_start(): 
    print ("left start")
    return "nothing"


@app.route('/left_stop')
def left_stop():
    print ("left stop")
    return "nothing"


@app.route('/right_start')
def right_start():
    print ("right start")
    return "nothing"


@app.route('/right_stop')
def right_stop():
    print ("right stop")
    return "nothing"


@app.route('/backward_start')
def backward_start():
    print ("backward start")  
    return "nothing"


@app.route('/backward_stop')
def backward_stop():
    print ("backward_stop")
    return "nothing"

@app.route('/exit')
def exit():
    print("exit")
    return "nothing"


if __name__ == "__main__":
    app.run(debug=True)
