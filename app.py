from flask import Flask,request
import os
import cv2 

app = Flask(__name__)
face_recognizer = cv2.face.EigenFaceRecognizer_create()
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('modeloLBPHFace.xml')
face_recognizer.read('modeloEigenFace.xml')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# ██████████████████████████████████████

@app.route('/', methods=['POST'])
def comprobate__coscu():
    try:
        coscu = False
        image = request.files['file']
        imageRoute = os.path.join(os.path.dirname(__file__), 'coscu.png') 
        image.save(imageRoute) 
        
        cap = cv2.VideoCapture('coscu.png')
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            coscu = True  
            print(result[1])
            print('cocu' if result[1] < 70 else 'no cocu')
        cap.release() 
        os.remove(imageRoute)
        return { "IsCoscu": coscu }
    except:
        return 'ingrese el archivo' 