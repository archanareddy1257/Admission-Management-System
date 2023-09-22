from tkinter import*
from tkinter import messagebox
import csv
import pandas as pd

def show_frame(frame):
    frame.tkraise()

window = Tk()
window.title(" COLLEGE INFORMATION SYSTEM ")
window.geometry('1000x1000')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)


frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame(window)
frame5 = Frame(window)
frame6 = Frame(window)
frame7 = Frame(window)
frame8 = Frame(window)
frame9 = Frame(window)
frame10 = Frame(window)
frame11 = Frame(window)
frame12 = Frame(window)
frame13 = Frame(window)


for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame12,frame13):
    frame.grid(row=0,column=0,sticky='nsew')

#  Main window (frame1)

frame1_btn1 = Button(frame1,text="INDIVIDUAL STUDENT DETAILS",bg="tan1",command=lambda:show_frame(frame2),width=30).place(x=270,y=50)
frame1_btn2 = Button(frame1,text="BRANCH WISE LIST OF STUDENTS",bg="cyan",command=lambda:show_frame(frame3),width=30).place(x=270,y=150)
frame1_btn3 = Button(frame1,text="CATEGORY WISE LIST OF STUDENTS",bg="indianred",command=lambda:show_frame(frame4),width=30).place(x=270,y=250)
#frame1_btn4 = Button(frame1,text="Go Back",bg = "blue",command=lambda:menu,width=15).place(x=330,y=450)

#    frame2===individual student info

def ex_info(a):
    f = open('student.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        if a == row[1]:
            output = "Name : %s \n ID : %s \n Gender : %s \n DOB : %s  \n Father's name : %s  \n Mother's name : %s \n EAMCET Rank : %s \n Spl reservation : %s \n Branch : %s" % (
                    row[0], row[1], row[13], row[7], row[4], row[3], row[10], row[11], row[2])
            messagebox.showinfo("Required Student Info ", output)
        else:
            messagebox.showinfo("Required Student Info ","Invalid ID")
            break

def get_info():
    set_info = f"{x.get()}"
    ex_info(set_info)

frame2_label1 = Label(frame2, text=" Admission details ", fg="white", bg="orange",  width=62).place(x=10, y=10)
frame2_label2 = Label(frame2, text=" Enter Candidate's ID", fg="black", bg="pink",width=40).place(x=50, y=70)

x = StringVar()
frame2_entry = Entry(frame2, textvariable=x, bg="white", font=("Arial", 20, "bold"), width=6).place(x=400, y=70)
frame2_btn = Button(frame2, text="Get Info", fg="white", bg="red",  width=15,command=get_info).place(x=300, y=150)


frame2_backbtn = Button(frame2, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame1),  width=15).place(x=300, y=200)

#   frame3===branchwise list

# frame5===cse

df1=pd.read_csv('CSE.csv')
df1.set_index('Name',inplace=True)
x1=df1[['Admission Number',	'Branch','Father Name','Mother Name']]
df1.set_index('caste',inplace=True)
y1 = df1[['Contact number']]
df1.set_index('DOB',inplace=True)
z1=df1[['10th CGPA','Inter marks','Eamcet rank','Special Category']]

frame5_label1= Label(frame5,text=x1,width=50).place(x=20,y=100)
frame5_label2= Label(frame5,text=y1,width=50).place(x=370,y=100)
frame5_label3= Label(frame5,text=z1,width=50).place(x=620,y=100)

frame5_backbtn = Button(frame5, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame3),  width=15).place(x=400, y=600)

df1.head()

#frame6===ece

df2=pd.read_csv('ECE.csv')
df2.set_index('Name',inplace=True)
x2=df2[['Admission Number',	'Branch','Father Name','Mother Name']]
df2.set_index('caste',inplace=True)
y2 = df2[['Contact number']]
df2.set_index('DOB',inplace=True)
z2=df2[['10th CGPA','Inter marks','Eamcet rank','Special Category']]

frame6_label1= Label(frame6,text=x2,width=50).place(x=20,y=100)
frame6_label2= Label(frame6,text=y2,width=50).place(x=370,y=100)
frame6_label3= Label(frame6,text=z2,width=50).place(x=620,y=100)

frame6_backbtn = Button(frame6, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame3),  width=15).place(x=400, y=600)

df2.head()

#frame7===eee

df3=pd.read_csv('EEE.csv')
df3.set_index('Name',inplace=True)
x3=df3[['Admission Number',	'Branch','Father Name','Mother Name']]
df3.set_index('caste',inplace=True)
y3 = df3[['Contact number']]
df3.set_index('DOB',inplace=True)
z3=df3[['10th CGPA','Inter marks','Eamcet rank','Special Category']]

frame7_label1= Label(frame7,text=x3,width=50).place(x=20,y=100)
frame7_label2= Label(frame7,text=y3,width=50).place(x=370,y=100)
frame7_label3= Label(frame7,text=z3,width=50).place(x=620,y=100)

frame7_backbtn = Button(frame7, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame3),  width=15).place(x=400, y=600)

df3.head()

#frame8===mech

df4=pd.read_csv('MECH.csv')
df4.set_index('Name',inplace=True)
x4=df4[['Admission Number',	'Branch','Father Name','Mother Name']]
df4.set_index('caste',inplace=True)
y4 = df4[['Contact number']]
df4.set_index('DOB',inplace=True)
z4=df4[['10th CGPA','Inter marks','Eamcet rank','Special Category']]

frame8_label1= Label(frame8,text=x4,width=50).place(x=20,y=100)
frame8_label2= Label(frame8,text=y4,width=50).place(x=370,y=100)
frame8_label3= Label(frame8,text=z4,width=50).place(x=620,y=100)

frame8_backbtn = Button(frame8, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame3),  width=15).place(x=400, y=600)

df4.head()

#frame9===civil

df5=pd.read_csv('CIVIL.csv')
df5.set_index('Name',inplace=True)
x5=df5[['Admission Number',	'Branch','Father Name','Mother Name']]
df5.set_index('caste',inplace=True)
y5 = df5[['Contact number']]
df5.set_index('DOB',inplace=True)
z5=df5[['10th CGPA','Inter marks','Eamcet rank','Special Category']]

frame9_label1= Label(frame9,text=x5,width=50).place(x=20,y=100)
frame9_label2= Label(frame9,text=y5,width=50).place(x=370,y=100)
frame9_label3= Label(frame9,text=z5,width=50).place(x=620,y=100)

frame9_backbtn = Button(frame9, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame3),  width=15).place(x=400, y=600)

df5.head()



frame3_btn1 = Button(frame3,text="CSE",command=lambda:show_frame(frame5),bg="skyblue",width=30).place(x=270,y=50)
frame3_btn2 = Button(frame3,text="ECE",command=lambda:show_frame(frame6),bg="skyblue",width=30).place(x=270,y=100)
frame3_btn3 = Button(frame3,text="EEE",command=lambda:show_frame(frame7),bg="skyblue",width=30).place(x=270,y=150)
frame3_btn4 = Button(frame3,text="MECH",command=lambda:show_frame(frame8),bg="skyblue",width=30).place(x=270,y=200)
frame3_btn5 = Button(frame3,text="CIVIL",command=lambda:show_frame(frame9),bg="skyblue",width=30).place(x=270,y=250)

frame3_backbtn = Button(frame3, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame1),  width=15).place(x=320, y=300)


#     frame4===categorywise list

# frame 10===oc

df6=pd.read_csv('OC.csv')
df6.set_index('Name',inplace=True)
x6=df6[['Admission number',	'Branch','Fathers name','Mothers name']]
df6.set_index('Caste',inplace=True)
y6 = df6[['Contact number']]
df6.set_index('DOB',inplace=True)
z6=df6[['10th CGPA','Inter marks','Eamcet Rank','Special category']]

frame10_label1= Label(frame10,text=x6,width=50).place(x=20,y=100)
frame10_label2= Label(frame10,text=y6,width=50).place(x=370,y=100)
frame10_label3= Label(frame10,text=z6,width=50).place(x=620,y=100)

frame10_backbtn = Button(frame10, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame4),  width=15).place(x=400, y=600)

df6.head()

# frame11===bc

df7=pd.read_csv('BC.csv')
df7.set_index('Name',inplace=True)
x7=df7[['Admission number',	'Branch','Fathers name','Mothers name']]
df7.set_index('Caste',inplace=True)
y7 = df7[['Contact number']]
df7.set_index('DOB',inplace=True)
z7=df7[['10th GPA','Inter marks','Eamcet rank','Special category']]

frame11_label1= Label(frame11,text=x7,width=50).place(x=20,y=100)
frame11_label2= Label(frame11,text=y7,width=50).place(x=370,y=100)
frame11_label3= Label(frame11,text=z7,width=50).place(x=620,y=100)

frame11_backbtn = Button(frame11, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame4),  width=15).place(x=400, y=600)

df7.head()

# frame 12===sc

df8=pd.read_csv('SC.csv')
df8.set_index('Name',inplace=True)
x8=df8[['Admission number',	'Branch','Fathers name','Mothers name']]
df8.set_index('Caste',inplace=True)
y8 = df8[['Contact number']]
df8.set_index('DOB',inplace=True)
z8=df8[['10th GPA','Inter marks','Eamcet rank','Special category']]

frame12_label1= Label(frame12,text=x8,width=50).place(x=20,y=100)
frame12_label2= Label(frame12,text=y8,width=50).place(x=370,y=100)
frame12_label3= Label(frame12,text=z8,width=50).place(x=620,y=100)

frame12_backbtn = Button(frame12, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame4),  width=15).place(x=400, y=600)

df8.head()

#frame 13===st

df9=pd.read_csv('ST.csv')
df9.set_index('Name',inplace=True)
x9=df9[['Admission number',	'Branch','Fathers name','Mothers name']]
df9.set_index('Caste',inplace=True)
y9 = df9[['Contact number']]
df9.set_index('DOB',inplace=True)
z9=df9[['10th GPA','Inter marks','Eamcet rank','Special category']]

frame13_label1= Label(frame13,text=x9,width=50).place(x=20,y=100)
frame13_label2= Label(frame13,text=y9,width=50).place(x=370,y=100)
frame13_label3= Label(frame13,text=z9,width=50).place(x=620,y=100)

frame13_backbtn = Button(frame13, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame4),  width=15).place(x=400, y=600)

df9.head()

frame4_btn1 = Button(frame4,text="OC",command=lambda:show_frame(frame10),bg="gold2",width=30).place(x=280,y=50)
frame4_btn2 = Button(frame4,text="BC",command=lambda:show_frame(frame11),bg="gold2",width=30).place(x=280,y=100)
frame4_btn3 = Button(frame4,text="SC",command=lambda:show_frame(frame12),bg="gold2",width=30).place(x=280,y=150)
frame4_btn4 = Button(frame4,text="ST",command=lambda:show_frame(frame13),bg="gold2",width=30).place(x=280,y=200)

frame4_backbtn = Button(frame4, text = "Back",fg="white", bg="purple",command=lambda:show_frame(frame1),  width=15).place(x=330, y=300)

show_frame(frame1)

window.mainloop()