from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+-10+0")
        self.root.title("Attendance file")
        # variables
        self.var_eid=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atd=StringVar()
        # 1st image
        img1=Image.open(r"images\frp_10.jpg")
        img1=img1.resize((384,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=384,height=150)
        # 2nd image
        img2=Image.open(r"images\frp_11.jpg")
        img2=img2.resize((384,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=384,y=0,width=384,height=150)
        # 3rd image
        img3=Image.open(r"images\frp_12.jpg")
        img3=img3.resize((384,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=768,y=0,width=384,height=150)
        # 4th image
        img4=Image.open(r"images\frp_13.jpg")
        img4=img4.resize((384,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1152,y=0,width=384,height=150)
        # backgroung image
        img=Image.open(r"images\frp_1.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=150,width=1920,height=930)
        # title
        title_lbl=Label(bg_img,text="Attendance",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1540,height=55)
        # frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=60,width=1515,height=577)
        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Attendance Details",font=("times new roman",15,"bold"))
        left_frame.place(x=5,y=10,width=750,height=560)
        # Employee ID 
        eid_label=Label(left_frame,text="Employee ID:",font=("times new roman",15,"bold"))
        eid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        # entry for Employee ID
        eid_entry=Entry(left_frame,width=25,textvariable=self.var_eid,font=("times new roman",12,"bold"))
        eid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        # Roll No
        roll_label=Label(left_frame,text="Roll No:",font=("times new roman",15,"bold"))
        roll_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        # entry for Roll No
        roll_entry=Entry(left_frame,width=25,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        # Name
        name_label=Label(left_frame,text="Name:",font=("times new roman",15,"bold"))
        name_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        # entry for Name
        name_entry=Entry(left_frame,width=25,textvariable=self.var_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        # Department 
        dept_label=Label(left_frame,text="Department:",font=("times new roman",15,"bold"))
        dept_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        # entry for Department
        dept_entry=Entry(left_frame,width=25,textvariable=self.var_dept,font=("times new roman",12,"bold"))
        dept_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        # Time
        time_label=Label(left_frame,text="Time:",font=("times new roman",15,"bold"))
        time_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        # entry for Time
        time_entry=Entry(left_frame,width=25,textvariable=self.var_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        # Date
        date_label=Label(left_frame,text="Date:",font=("times new roman",15,"bold"))
        date_label.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        # entry for Date
        date_entry=Entry(left_frame,width=25,textvariable=self.var_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)
        # Attendance Status
        atd_label=Label(left_frame,text="Attendance Status",font=("times new roman",15,"bold"))
        atd_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        # combo box for Attendance Status
        atd_combo=ttk.Combobox(left_frame,width=25,textvariable=self.var_atd,font=("times new roman",12,"bold"),state="readonly")
        atd_combo["values"]=("Status","Present","Absent")
        atd_combo.current(0)
        atd_combo.grid(row=6,column=1,padx=10,pady=10,sticky=W)
        # buttoms frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=425,width=745,height=35)
        # buttons
        import_btn=Button(btn_frame,text="Import csv",command=self.importCSV,width=20,font=("times new roman",12,"bold"),bg="light blue")
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCSV,width=20,font=("times new roman",12,"bold"),bg="light blue")
        export_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text="Update",width=20,font=("times new roman",12,"bold"),bg="light blue")
        update_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",12,"bold"),bg="light blue")
        reset_btn.grid(row=0,column=3)
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",15,"bold"))
        right_frame.place(x=765,y=10,width=740,height=560)
        # table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,font=("times new roman",15,"bold"))
        table_frame.place(x=10,y=10,width=720,height=500)
        # x-axis scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # y-axis scroll bar
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("eid","roll","name","dept","time","date","atd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("eid",text="Employee ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dept",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("atd",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("eid",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dept",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("atd",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    # fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    # importCSV function
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    # ExportCSV function
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_eid.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dept.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atd.set(rows[6])
    # reset function
    def reset_data(self):
        self.var_eid.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atd.set("Status")

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
