import cv2

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_detector = cv2.CascadeClassifier("haarcascade_smile.xml")

webcam = cv2.VideoCapture(1)

while True:
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        face_gray = gray_frame[y:y+h, x:x+w]
        smiles = smile_detector.detectMultiScale(face_gray, scaleFactor=1.7, minNeighbors=20)

        for (x_, y_, w_, h_) in smiles:
            #cv2.rectangle(frame, (x+x_, y+y_), (x+x_+w_, y+y_+h_), (255, 0, 0), 4)
            cv2.putText(frame, 'Smiling', (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
