import cv2
from keras.models import load_model
import numpy as np

model = load_model('emotion_model.h5')

emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}
cap = cv2.VideoCapture(0)

def get_emotion():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(gray_frame, 1.3, 5)

