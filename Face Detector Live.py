import tkinter as tk
import cv2
from PIL import Image,ImageTk
 

def face_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,minNeighbors = 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(255,0,0),2)
        cv2.putText(frame,"Live Human",(x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9 , (36,255,12),2)
    
    return frame

def Open_Camera():
    Capturing = cv2.VideoCapture(0)
    if not Capturing.isOpened():
        print("Error: Unable To Open Camera.")
        return
    while True :
        ret,frame = Capturing.read()
        if not ret:
            print("Erorr: Unable To Capture.")
            break
        frame = cv2.resize(frame,(800,600))
        frame = face_detection(frame)

        cv2.imshow("Face Detection",frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            Capturing.release()
            cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

AppWindow = tk.Tk()
AppWindow.configure(bg="black")
AppWindow.geometry("300x250")
AppWindow.resizable(0,0)
AppWindow.title("Live Face Scanner")
Camera_Button = tk.Button(AppWindow,text="Open Camera",font=("boulder","17","bold"),bg="white",fg="black",command=Open_Camera)
Camera_Button.pack(padx=70,pady=70)

AppWindow.mainloop()




    


    