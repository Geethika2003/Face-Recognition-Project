
----------------------------Face-Recognition-Project-----------------------------

This is a Facial Recognition System for Attendance tracking.
In this project for front end we used Tkinter GUI and for back end python programming.
Here we created a desktop based application for attendance tracking.

Basically there are few steps involved in this project:
1)Generating Data Set
2)Train the Classifier
3)Face Detecting
4)Tracking Attendance

There are five buttons in this application they are:

First button is Student details if we click this button a new window will be opened  in tis we can enter the details of the students and save them so that they will be
saved int he window as well as in mysql workbench. We can delete any student details. we can update any student details. we can reset the values. we can also give the
photo samples if we want. The given photo samples will be stored in data folder.

Second button is Student Photos the above data folder can be directly accessed from this button.

Third button is Train data, if we click this button a new window will be opened. In this window there is a button called train data if we click this button the system
will be trained with the student photos in data folder.

Fourth button is Face Detector if we click this button a new window will be opened and in that window there is button named Face Recognition if we click that our
system's webcam will be opened and it will recognize person's face and mark her/him as preset along with the respective date and time and that information will be
stored in a .csv file and a excel file.

Fifth button is Attendance. if we click this button a new window will be opened. In that window there will be attendance details of the students. we can import csv
file and export the csv file we can update and delete data.
