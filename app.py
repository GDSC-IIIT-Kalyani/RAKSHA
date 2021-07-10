import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg)
# from camera_pi import Camera
from camera import Camera
from scoring import get_score

app = Flask(__name__)

category = 'Hammer Strike'


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        img = frame
        yield (b'--mySplitter\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/k')
def leaderboard():
    return render_template('k.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/pose')
def pose():
    """Video streaming home page."""
    return render_template('pose.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=mySplitter')
                    
@app.route('/update')
def update_score():
    return render_template('pose.html', score=get_score(category))              

if __name__ == '__main__':
    app.run(debug=True, threaded=True)