import cv2
import os
import numpy as np

dataPath = 'C:/Users/danie/Desktop/proyect/cosculike 2/IA' 
labels = []
facesData = []

print('Leyendo las imágenes')
for fileName in os.listdir(dataPath + '/' + 'Coscu'):
    print('Rostros: ', 'Coscu' + '/' + fileName)
    labels.append(0)
    facesData.append(cv2.imread('Coscu' +'/'+ fileName,0))


# Métodos para entrenar el reconocedor
# face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
# face_recognizer.write('modeloEigenFace.xml')
face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado...")