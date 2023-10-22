#dar un menu amigable para elegir las fuentes de video, y asignar un nombre a la persona en personaName
#importo las librerias necesarias
import cv2
import os
import imutils
#creo una funcion para ver si el nombre de la carpeta esta diponible
def carpetaDisponible(personName):
    dataPath='data'
    personPath=dataPath + '/' + personName
    if not os.path.exists(personPath):
        return True
    else:
        return False


personName=input("ingrese el nombre de la persona: ")
dataPath='data'
personPath=dataPath + '/' + personName
#print person path
while carpetaDisponible(personName) == False:
    print('El nombre de la carpeta ya existe, ingrese otro nombre')
    personName=input("ingrese el nombre de la persona: ")
    personPath=dataPath + '/' + personName
    print(personPath)
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)
#creo una lista con los videos disponibles en dataEntris
videos=os.listdir('dataEntris')
print('Lista de videos: ',videos)
#creo un menu para elegir el video
print('Elija el video que desea utilizar')
for i in range(len(videos)):
    print(i,'-',videos[i])
video=int(input('Ingrese el numero del video: '))
#creo una variable con el nombre del video elegido
videoName=videos[video]
#creo una variable con la ruta del video elegido
videoPath='dataEntris/'+videoName
cap=cv2.VideoCapture(videoPath)
faceClassif=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count=0
while True:
    ret,frame=cap.read()
    if ret==False:break
    frame=imutils.resize(frame,width=640)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    auxFrame=frame.copy()
    faces=faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        rostro=auxFrame[y:y+h,x:x+w]
        rostro=cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath+'/rostro_{}.jpg'.format(count),rostro)
        count=count+1
    cv2.imshow('frame',frame)
    k=cv2.waitKey(1)
    if k==27 or count>=300:
        break
cap.release()
cv2.destroyAllWindows()
#muevo el video capturado a la carpeta capturados
print("dataEntris/"+videoName)

os.replace("dataEntris/"+videoName ,"dataEntries/capturados/"+videoName)    
#creo un archivo txt con el nombre de la persona
archivo=open(personPath+'/nombre.txt','w')
archivo.write(personName)
archivo.close()
#creo un archivo txt con el nombre del video
archivo=open(personPath+'/video.txt','w')
archivo.write(videoName)
archivo.close()
