from flask import Flask, render_template, jsonify, request
from emotion_detection import get_emotion
from playlist import play_music

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_emotion', methods=['GET'])
def detect_emotion():
    emotion = get_emotion()  # Get emotion from your OpenCV model
    return jsonify({'emotion': emotion})

@app.route('/play_music', methods=['POST'])
def play_music_route():
    data = request.get_json()
    emotion = data['emotion']
    play_music(emotion)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
