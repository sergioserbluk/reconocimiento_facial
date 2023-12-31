import cv2
from cv2 import eigen
import os
import numpy as np
dataPath='data'
peopleList=os.listdir(dataPath)
print('Lista de personas: ',peopleList)
labels=[]
facesData=[]
label=0
for nameDir in peopleList:
    personPath=dataPath+'/'+nameDir
    print('Leyendo las imagenes')
    for fileName in os.listdir(personPath):
        print('Rostros: ',nameDir+'/'+fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image=cv2.imread(personPath+'/'+fileName,0)
        cv2.imshow('image',image)
        cv2.waitKey(10)
    label=label+1
print('labels= ',labels)
print('Numero de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
face_recognizer=cv2.face.EigenFaceRecognizer_create() 
#Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData,np.array(labels))
#Almacenando el modelo obtenido
face_recognizer.write('modeloEigenFace.xml')
print("Modelo almacenado...")
cv2.destroyAllWindows()