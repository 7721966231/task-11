from flask import Flask, jsonify, request
from emotion_detection import get_emotion  # Assume this function returns the detected emotion
from playlist import play_music

app = Flask(__name__)

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
import logging

logging.basicConfig(level=logging.INFO)

@app.route('/detect_emotion', methods=['GET'])
def detect_emotion():
    try:
        emotion = get_emotion()  # Get emotion from your OpenCV model
        logging.info(f"Detected emotion: {emotion}")
        return jsonify({'emotion': emotion})
    except Exception as e:
        logging.error(f"Error detecting emotion: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/play_music', methods=['POST'])
def play_music_route():
    try:
        data = request.get_json()
        emotion = data['emotion']
        logging.info(f"Playing music for emotion: {emotion}")
        play_music(emotion)
        return '', 204
    except Exception as e:
        logging.error(f"Error playing music: {str(e)}")
        return jsonify({'error': str(e)}), 500