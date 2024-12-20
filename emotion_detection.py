import cv2
import numpy as np
from keras.models import load_model
import face_recognition

# Load the emotion detection model
model = load_model('models/emotion_model.h5')

# Define emotion categories
emotion_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load a sample picture and learn how to recognize it.
image = face_recognition.load_image_file("known_faces/known_person.jpg")
face_encoding = face_recognition.face_encodings(image)[0]

# Add the face encoding and name to the known lists
known_face_encodings.append(face_encoding)
known_face_names.append("Person Name")

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Start the webcam feed
cap = cv2.VideoCapture(0)

def get_emotion():
    global face_locations, face_encodings, face_names, process_this_frame
    ret, frame = cap.read()
    if not ret:
        return "None"

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml').detectMultiScale(gray_frame, 1.3, 5)
    
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        emotion_prediction = model.predict(cropped_img)
        max_index = int(np.argmax(emotion_prediction))
        emotion = emotion_dict[max_index]
        
        cv2.putText(frame, f'{name} - {emotion}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return emotion

if __name__ == "__main__":
    while True:
        emotion = get_emotion()
        print(f"Detected Emotion: {emotion}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
