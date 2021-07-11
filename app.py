import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


from flask import Flask, render_template, Response, request

# from camera_pi import Camera
from camera import Camera
from scoring import get_score

app = Flask(__name__)

global category


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

@app.route('/pose', methods=['GET', 'POST'])
def pose():
    global category
    """Video streaming"""
    category = request.form.get('detect')
    return render_template('pose.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=mySplitter')
                    
@app.route('/update', methods=['GET', 'POST'])
def update_score():
    return render_template('score.html', score=get_score(category))        

@app.route('/record_status', methods=['POST'])
def record_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")      

if __name__ == '__main__':
    app.run(debug=True, threaded=True)