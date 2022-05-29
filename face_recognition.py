from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+-10+0")
        self.root.title("Face Recognizer")
        # title
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1540,height=55)
        # images
        img=Image.open(r"images\frp_16.jpg")
        img=img.resize((650,750),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=650,height=750)
        img1=Image.open(r"images\frp_17.jpg")
        img1=img1.resize((890,750),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=55,width=890,height=750)
        # button
        bt=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="black")
        bt.place(x=370,y=680,width=200,height=50)
    # attendance
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

    # Face recognition fucntion
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
                my_cursor=conn1.cursor()
                my_cursor.execute("select name from student where student_ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                my_cursor.execute("select roll_no from student where student_ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                my_cursor.execute("select department from student where student_ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                my_cursor.execute("select student_ID from student where student_ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                if confidence>77:
                    cv2.putText(img,f"student_ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"roll_no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)                   
                    cv2.putText(img,f"department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)                   
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
