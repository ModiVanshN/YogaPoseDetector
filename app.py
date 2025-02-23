from flask import Flask, render_template, Response, request
from pose_detector import detect_pose
from timer import Timer
import cv2

app = Flask(__name__)
timer = Timer()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pose_detector')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_pose(timer), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    timer.start()
    return '', 204

@app.route('/stop_timer', methods=['POST'])
def stop_timer():
    timer.stop()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
