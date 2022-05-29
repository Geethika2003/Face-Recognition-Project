from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+-10+0")
        self.root.title("Student Details")
        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_state=StringVar()
        self.var_t_name=StringVar()
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
        title_lbl=Label(bg_img,text="STUDENT DETAILS MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=220,y=0,width=1080,height=40)
        # frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1515,height=580)
        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Details",font=("times new roman",15,"bold"))
        left_frame.place(x=5,y=10,width=750,height=560)
        # current course frame
        cc_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        cc_frame.place(x=5,y=5,width=735,height=130)
        # department label
        dp_label=Label(cc_frame,text="Deparment",font=("times new roman",15,"bold"))
        dp_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        # combo box of Department
        dp_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dp_combo["values"]=("Select Department","CSE","ECE","EEE","Mech","Civil","Chem","Bio","MME")
        dp_combo.current(0)
        dp_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        # Course
        course_label=Label(cc_frame,text="Course",font=("times new roman",15,"bold"))
        course_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        # combo box of Course 
        course_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","M.Sc.","M.B.A","M.C.A")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        # year
        year_label=Label(cc_frame,text="Year",font=("times new roman",15,"bold"))
        year_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        # combo box of Year
        year_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        # Semester
        sem_label=Label(cc_frame,text="Semester",font=("times new roman",15,"bold"))
        sem_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        # combo box for Semester
        sem_combo=ttk.Combobox(cc_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","1","2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        # class student information frame
        cs_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
        cs_frame.place(x=5,y=140,width=735,height=385)
        # student ID 
        sid_label=Label(cs_frame,text="Student ID:",font=("times new roman",15,"bold"))
        sid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        # entry for student ID
        sid_entry=Entry(cs_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        sid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        # student name
        name_label=Label(cs_frame,text="Name:",font=("times new roman",15,"bold"))
        name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        # entry for student name
        name_entry=Entry(cs_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        # student class division
        cd_label=Label(cs_frame,text="Class Division:",font=("times new roman",15,"bold"))
        cd_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        # combo box of student class division
        div_combo=ttk.Combobox(cs_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        # student Roll No
        rollno_label=Label(cs_frame,text="Roll No:",font=("times new roman",15,"bold"))
        rollno_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        # entry for student Roll No
        rollno_entry=Entry(cs_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        # student Email
        email_label=Label(cs_frame,text="Email:",font=("times new roman",15,"bold"))
        email_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        # entry for student Email
        email_entry=Entry(cs_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        # student Gender
        gender_label=Label(cs_frame,text="Gender:",font=("times new roman",15,"bold"))
        gender_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        # combo box of student Gender
        gender_combo=ttk.Combobox(cs_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        # student DOB
        dob_label=Label(cs_frame,text="Date of Birth:",font=("times new roman",15,"bold"))
        dob_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        # entry for student DOB
        dob_entry=Entry(cs_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        # student Phone No
        pno_label=Label(cs_frame,text="Phone No:",font=("times new roman",15,"bold"))
        pno_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        # entry for student Phone No
        pno_entry=Entry(cs_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        pno_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)
        # student State
        state_label=Label(cs_frame,text="State:",font=("times new roman",15,"bold"))
        state_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        # entry for student State
        state_entry=Entry(cs_frame,textvariable=self.var_state,width=20,font=("times new roman",12,"bold"))
        state_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)
        # student's Teacher name
        teacher_label=Label(cs_frame,text="Teacher Name:",font=("times new roman",15,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)
        # entry for student's Teacher name
        teacher_entry=Entry(cs_frame,textvariable=self.var_t_name,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        radiobtn2=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=10,sticky=W)
        # buttoms frame
        btn_frame=Frame(cs_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=5,y=275,width=719,height=35)
        # buttons
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="light blue")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="light blue")
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="light blue")
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="light blue")
        reset_btn.grid(row=0,column=3)
        # buttons frame
        btn1_frame=Frame(cs_frame,bd=2,relief=RIDGE)
        btn1_frame.place(x=20,y=320,width=690,height=35)
        take_photo_btn1=Button(btn1_frame,command=self.generate_dataset,text="Take photo Sample",width=37,font=("times new roman",12,"bold"),bg="light blue")
        take_photo_btn1.grid(row=0,column=0)
        update_photo_btn1=Button(btn1_frame,text="Update photo Sample",width=37,font=("times new roman",12,"bold"),bg="light blue")
        update_photo_btn1.grid(row=0,column=1)
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Details",font=("times new roman",15,"bold"))
        right_frame.place(x=765,y=10,width=740,height=560)
        # search system
        # serach frame
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        search_frame.place(x=10,y=0,width=720,height=80)
        # search 
        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        # combo box for search
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        # entry
        search_entry=Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        # buttons
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="light blue")
        search_btn.grid(row=0,column=3)
        showall_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="light blue")
        showall_btn.grid(row=0,column=4,padx=5)
        # table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,font=("times new roman",15,"bold"))
        table_frame.place(x=10,y=85,width=720,height=445)
        # x-axis scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # y-axis scroll bar
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","roll","email","gender","dob","phone","state","tname","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("state",text="State")
        self.student_table.heading("tname",text="Teacher Name")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("state",width=100)
        self.student_table.column("tname",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
    # function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
                my_cursor=conn1.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_state.get(),
                                                                                                                self.var_t_name.get(),
                                                                                                                self.var_radio1.get()
                                                                                                         ))    
                conn1.commit()
                self.fetch_data()
                conn1.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # fetch data
    def fetch_data(self):
        conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
        my_cursor=conn1.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn1.commit()
        conn1.close()
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_email.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_state.set(data[12]),
        self.var_t_name.set(data[13]),
        self.var_radio1.set(data[14])
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update1=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update1>0:
                    conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
                    my_cursor=conn1.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,email=%s,gender=%s,DOB=%s,phone_no=%s,state=%s,t_name=%s,photo_uploaded=%s where student_ID=%s",(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_state.get(),
                                                                                                                                                                                                                                self.var_t_name.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                                             ))
                else:
                    if not Update1:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn1.commit()
                self.fetch_data()
                conn1.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root) 
                if delete>0:
                    conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
                    my_cursor=conn1.cursor()
                    sql="delete from student where student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn1.commit()
                self.fetch_data()
                conn1.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    # reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_state.set("")
        self.var_t_name.set("")
        self.var_radio1.set("")
    # Generate data set or Take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn1=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="face_recognition_project")
                my_cursor=conn1.cursor()
                my_cursor.execute("select * from student")
                myresults=my_cursor.fetchall()
                id=0
                for x in myresults:
                    id+=1
                my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll_no=%s,email=%s,gender=%s,DOB=%s,phone_no=%s,state=%s,t_name=%s,photo_uploaded=%s where student_ID=%s",(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_state.get(),
                                                                                                                                                                                                                                self.var_t_name.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                                             ))
                conn1.commit()
                self.fetch_data()
                self.reset_data()
                conn1.close()
                # Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3 and minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()