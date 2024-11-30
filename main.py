# why import like this ---> call predefined fun without its class
from db import Database   # import my user defined module

from tkinter import ttk   
from tkinter import messagebox
from tkinter import *
import tkinter as tk

db=Database("mpc")   
root = Tk() # create root window
root.title("Student Management System")
root.geometry("1920x1080+0+0")  #0 --> x,y axis 0
root.config(bg="white") # root window color
root.state("zoomed")  # maximize

Rollno=StringVar()      #Intvar,DoubleVar
Name=StringVar()        # which type will pass in that text box
DOB=StringVar()         
Gender=StringVar()
Mark10th=StringVar()
JoinDate=StringVar()
dept=StringVar()
contact=StringVar()
address=StringVar()


# in tk , all are widigit
# Entry Frame
entries_frame = Frame(root, bg="#4F3F84") # create frame like container , color-->purple 
entries_frame.pack(side=TOP, fill=X) # add this frame in window , TOP (default), BOTTOM, LEFT, or RIGHT. fill=X rowspan that fill x axis

title = Label(entries_frame, text="Student Management System", font=("Calibri", 18, "bold"), bg="#4F3F84", fg="white")  #fg-->font color
title.grid(row=0, columnspan=3, padx=10, pady=20, sticky="w")  # rows and columns  , w,e,n,s

lblrollno = Label(entries_frame, text="Rollno", font=("Calibri", 16), bg="#4F3F84", fg="white") # create lable
lblrollno.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtrollno = Entry(entries_frame, textvariable=Rollno, font=("Calibri", 16), width=30)  # input text box
txtrollno.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblname = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#4F3F84", fg="white")
lblname.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtname = Entry(entries_frame, textvariable=Name, font=("Calibri", 16), width=30)
txtname.grid(row=1, column=3, padx=10, pady=10, sticky="w")


lbldob = Label(entries_frame, text="DOB", font=("Calibri", 16), bg="#4F3F84", fg="white")
lbldob.grid(row=1, column=4, padx=10, pady=10, sticky="w")
txtdob = Entry(entries_frame, textvariable=DOB, font=("Calibri", 16), width=30)
txtdob.grid(row=1, column=5, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#4F3F84", fg="white")
lblGender.grid(row=2, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Gender, state="readonly")
comboGender['values'] = ("Male", "Female","others")  # if you add something add in () 
comboGender.grid(row=2, column=1, padx=10, sticky="w")

lblMark_10th = Label(entries_frame, text="Mark10th", font=("Calibri", 16), bg="#4F3F84", fg="white")
lblMark_10th.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtMark_10th = Entry(entries_frame, textvariable=Mark10th, font=("Calibri", 16), width=30)
txtMark_10th.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblJoinDate = Label(entries_frame, text="JoinDate", font=("Calibri", 16), bg="#4F3F84", fg="white")
lblJoinDate.grid(row=2, column=4, padx=10, pady=10, sticky="w")
txtJoinDate= Entry(entries_frame, textvariable=JoinDate, font=("Calibri", 16), width=30)
txtJoinDate.grid(row=2, column=5, padx=10, pady=10, sticky="w")

lbldept = Label(entries_frame, text="Department", font=("Calibri", 16), bg="#4F3F84", fg="white")
lbldept.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtdept = Entry(entries_frame, textvariable=dept, font=("Calibri", 16), width=30)
txtdept.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblcontact = Label(entries_frame, text="Contact", font=("Calibri", 16), bg="#4F3F84", fg="white")
lblcontact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtcontact= Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtcontact.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lbladdress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#4F3F84", fg="white")
lbladdress.grid(row=3, column=4, padx=10, pady=10, sticky="w")
txtaddress= Entry(entries_frame, textvariable=address, font=("Calibri", 16), width=30)
txtaddress.grid(row=3, column=5, padx=10, pady=10, sticky="w")



def getdata(e):   #get particular data when i click
    selected_row=tv.focus() # selece when focus
    data = tv.item(selected_row)  # get all item in seleced row
    global row
    row =data["values"]   #get all values
    Rollno.set(row[0])
    Name.set(row[1])
    DOB.set(row[2])
    Gender.set(row[3])
    Mark10th.set(row[4])
    JoinDate.set(row[5])
    dept.set(row[6])
    contact.set(row[7])
    address.set(row[8])





def displayAll():   # display all data
    #tv.delete(*tv.get_children())
    for child in tv.get_children():  #GET ALL DATA
        tv.delete(child)             #once insert after delete it

    for row in db.fetch():
        #print(type(row))  #tuple
        tv.insert("", END, values=row)  # ""--> new row , insert in end of row

def add_student():  # add student record
    if txtrollno.get() == "" or txtname.get() == "" or txtdob.get() == "" or comboGender.get() == "" or txtMark_10th.get() == "" or txtJoinDate.get() == "" or txtdept.get() == "" or txtcontact.get()=="" or txtaddress.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return  # display error after exits
    db.insert(txtrollno.get(),txtname.get(),txtdob.get(),comboGender.get(),txtMark_10th.get(),txtJoinDate.get(),txtdept.get(),txtcontact.get(),txtaddress.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()
    

def update_student(): # update data
    if txtrollno.get() == "" or txtname.get() == "" or txtdob.get() == "" or comboGender.get() == "" or txtMark_10th.get() == "" or txtJoinDate.get() == "" or txtdept.get() == "" or txtcontact.get()=="" or txtaddress.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtname.get(),txtdob.get(),comboGender.get(),txtMark_10th.get(),txtJoinDate.get(),txtdept.get(),txtcontact.get(),txtaddress.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    displayAll()


def delete_student():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():   # clear all data in fields
    Rollno.set("")
    Name.set("") 
    DOB.set("") 
    Gender.set("")
    Mark10th.set("")
    JoinDate.set("")
    dept.set("")
    contact.set("")
    address.set("")

#create buttons with seperate frame
btn_frame = Frame(entries_frame, bg="#4F3F84")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_student, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_student, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_student, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)


tree_frame = Frame(root, bg="#ecf0f1")    # create data display frame 
tree_frame.place(x=0, y=294, width=1550, height=1520)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),   # mystyle.Treeview name of style
                rowheight=50)  # Modify the font of the body (FOR DATA)  foreground="red" ,background="red"
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings(FOR HEADING)


# Create the Treeview widget
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), style="mystyle.Treeview") #create tree view its like table format

# Define headings and set column widths
tv.heading(1, text="Rollno", anchor="center")  # 1 --> column number
tv.column(1, width=100, anchor="center")    #w,e,n,s
tv.heading(2, text="Name", anchor="center")
tv.column(2, width=200 ,anchor="center")  # Adjusted width
tv.heading(3, text="DOB" ,anchor="center")
tv.column(3, width=150 ,anchor="center")  # Adjusted width
tv.heading(4, text="Gender" ,anchor="center")
tv.column(4, width=100 ,anchor="center")  # Adjusted width
tv.heading(5, text="Mark10th" ,anchor="center")
tv.column(5, width=100 ,anchor="center")  # Adjusted width
tv.heading(6, text="JoinDate" ,anchor="center")
tv.column(6, width=150 ,anchor="center")  # Adjusted width
tv.heading(7, text="Department" ,anchor="center")
tv.column(7, width=150 ,anchor="center")  # Adjusted width
tv.heading(8, text="Contact" ,anchor="center")
tv.column(8, width=150 ,anchor="center")  # Adjusted width
tv.heading(9, text="Address" ,anchor="center")
tv.column(9, width=250 ,anchor="center")  # Adjusted width

tv['show'] = 'headings'  #ONLY SHOW HEADINGS AVOID BLANK SPACE
tv.bind("<ButtonRelease-1>",getdata)     #create event if i click the data call getdata()
tv.pack(fill=tk.BOTH, expand=True)  # Adjusted the fill and expand options





displayAll()
#displayAll()
root.mainloop()