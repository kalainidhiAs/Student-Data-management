from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("student.db")
root = Tk()
root.title("STUDENT DATA MANAGEMENT")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

#defining variables
name = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
phone = StringVar()
address = StringVar()
enrolment_no = StringVar()
grade = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)

title = Label(entries_frame, text="Student Data Management", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=4, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblDob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
lblDob.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtDob = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
txtDob.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=2, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female", "Other")
comboGender.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblPhone = Label(entries_frame, text="Phone", font=("Calibri", 16), bg="#535c68", fg="white")
lblPhone.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtPhone = Entry(entries_frame, textvariable=phone, font=("Calibri", 16), width=30)
txtPhone.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblGrade = Label(entries_frame, text="Grade", font=("Calibri", 16), bg="#535c68", fg="white")
lblGrade.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtGrade = Entry(entries_frame, textvariable=grade, font=("Calibri", 16), width=30)
txtGrade.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lblEnrolment = Label(entries_frame, text="Enrolment No", font=("Calibri", 16), bg="#535c68", fg="white")
lblEnrolment.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtEnrolment = Entry(entries_frame, textvariable=enrolment_no, font=("Calibri", 16), width=30)
txtEnrolment.grid(row=4, column=1, padx=10, pady=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, width=50, height=5, font=("Calibri", 16))
txtAddress.grid(row=4, column=3, padx=10, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    
    name.set(row[1])
    dob.set(row[2])
    gender.set(row[3])
    email.set(row[4])
    phone.set(row[5])
    address.set(row[6])
    enrolment_no.set(row[7])
    grade.set(row[8])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[6]) 

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('', 'end', values=row)

def add_student():
    if txtName.get() == "" or txtDob.get() == "" or comboGender.get() == "" or txtEmail.get() == "" or txtPhone.get() == "" or txtAddress.get(
        1.0, END) == "" or txtEnrolment.get() == "" or txtGrade.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    db.insert(txtName.get(),txtDob.get(),comboGender.get(),txtEmail.get(),txtPhone.get(),txtAddress.get(
            1.0, END),txtEnrolment.get(),txtGrade.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()

def update_student():
    if txtName.get() == "" or txtDob.get() == "" or comboGender.get() == "" or txtEmail.get() == "" or txtPhone.get() == "" or txtAddress.get(
        1.0, END) == "" or txtEnrolment.get() == "" or txtGrade.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    db.update(row[0],txtName.get(),txtDob.get(),comboGender.get(),txtEmail.get(),txtPhone.get(),txtAddress.get(
            1.0, END),txtEnrolment.get(),txtGrade.get())
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()

def delete_student():
    if not row:
        messagebox.showerror("Error", "Please select a record to delete")
        return
    db.remove(row[0])
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    dob.set("")
    gender.set("")
    email.set("")
    phone.set("")
    address.set("")
    enrolment_no.set("")
    grade.set("")

btn_frame = Frame(entries_frame, background="#535c68")
btn_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="W")

btnAdd = Button(btn_frame, command=add_student, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085").grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_student, text="Update Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#1c7ec0").grid(row=0, column=1,padx=12)
btnDelete = Button(btn_frame, command=delete_student, text="Delete Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#c44320").grid(row=0, column=2,padx=12)
btnClear = Button(btn_frame, command=clearAll, text="Clear All", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="orange").grid(row=0, column=3,padx=12)

#table frame
tree_frame = Frame(root, bg="white")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body

tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8,9), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.heading("2", text="Name")
tv.heading("3", text="DOB")
tv.heading("4", text="Gender")
tv.heading("5", text="E-Mail")
tv.heading("6", text="Phone")
tv.heading("7", text="Address")
tv.heading("8", text="Enroll NO")
tv.heading("9", text="Grade")
tv['show'] = 'headings'


tv.column("1", width=10) 
tv.column("2", width=15) 
tv.column("3", width=15)  
tv.column("4", width=4) 
tv.column("5", width=20) 
tv.column("6", width=10) 
tv.column("7", width=30) 
tv.column("8", width=150)
tv.column("9", width=100) 

tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)


displayAll()
root.mainloop()
