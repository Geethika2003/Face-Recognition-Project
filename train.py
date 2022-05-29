from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+-10+0")
        self.root.title("Train Data")
        # title
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        # top images
        # 1st image
        img1=Image.open(r"images\frp_2.jpg")
        img1=img1.resize((384,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=384,height=150)
        # 2nd image
        img2=Image.open(r"images\frp_3.jpg")
        img2=img2.resize((384,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=384,y=45,width=384,height=150)
        # 3rd image
        img3=Image.open(r"images\frp_4.jpg")
        img3=img3.resize((384,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=768,y=45,width=384,height=150)
        # 4th image
        img4=Image.open(r"images\frp_5.jpg")
        img4=img4.resize((384,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1152,y=45,width=384,height=150)
        # button
        b=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="light blue",fg="black")
        b.place(x=0,y=195,width=1540,height=60)
        # bottom image
        img=Image.open(r"images\frp_15.jpg")
        img=img.resize((1540,500),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=240,width=1540,height=600)
    # function
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed.")


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()