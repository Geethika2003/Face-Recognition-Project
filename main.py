from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student import Student
from train import Train 
from face_recognition import Face_recognition
from Attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+-10+0")
        self.root.title("Face Recognition System")
        # 1st image
        img1=Image.open(r"images\frp_2.jpg")
        img1=img1.resize((384,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=384,height=150)
        # 2nd image
        img2=Image.open(r"images\frp_3.jpg")
        img2=img2.resize((384,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=384,y=0,width=384,height=150)
        # 3rd image
        img3=Image.open(r"images\frp_4.jpg")
        img3=img3.resize((384,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=768,y=0,width=384,height=150)
        # 4th image
        img4=Image.open(r"images\frp_5.jpg")
        img4=img4.resize((384,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1152,y=0,width=384,height=150)
        # backgroung image
        img=Image.open(r"images\frp_1.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=150,width=1920,height=1080)
        # title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=220,y=0,width=1080,height=40)
        # student button
        img5=Image.open(r"images\frp_6.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=105,y=150,width=200,height=200)
        b11=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="white",fg="black")
        b11.place(x=105,y=350,width=200,height=40)
        # face recognition button
        img6=Image.open(r"images\frp_7.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=390,y=250,width=200,height=200)
        b21=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="white",fg="black")
        b21.place(x=390,y=450,width=200,height=40)
        # attendance button
        img7=Image.open(r"images\frp_8.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Attendance)
        b3.place(x=675,y=150,width=200,height=200)
        b31=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance,font=("times new roman",20,"bold"),bg="white",fg="black")
        b31.place(x=675,y=350,width=200,height=40)
        # student photos button
        img8=Image.open(r"images\frp_9.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b4=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b4.place(x=960,y=250,width=200,height=200)
        b41=Button(bg_img,text="Student Photos",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bg="white",fg="black")
        b41.place(x=960,y=450,width=200,height=40)
        # train data button
        img9=Image.open(r"images\frp_14.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b5.place(x=1245,y=150,width=200,height=200)
        b51=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bg="white",fg="black")
        b51.place(x=1245,y=350,width=200,height=40)
    def open_img(self):
        os.startfile("data")
    # functions buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


