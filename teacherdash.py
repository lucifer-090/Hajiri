
import tkinter as tk
from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

t=tk.Tk()
t.title('Teachers Dashboarrd')
t.geometry("1400x800")
t.config(bg='#9e9e9e')


from PIL import Image,ImageTk
teach_dash=Image. open ("/Users/lucifer/Desktop/Alpha/teachdash.jpg")
resized_std = teach_dash.resize ((380,200))
converted_std=ImageTk. PhotoImage(resized_std)
teach_label=Label(t , image=converted_std,width=380,height=200,bg='#9e9e9e')
teach_label.place(x=30,y=10)


teaching_img=Image. open ("/Users/lucifer/Desktop/Alpha/teach.jpg")
resized_class = teaching_img.resize ((930,600))
converted_class=ImageTk. PhotoImage(resized_class)
teaching_label=Label(t , image=converted_class,width=930,height=600,bg='#9e9e9e')
teaching_label.place(x=260,y=180)

line=Frame(t, bg='black',height=3,width=1300)
line.place(x=40,y=205)

def prof():
    t=Tk()
    t.title('Your Profile')
    t.geometry('400x480')
    t.config(bg='powder blue')
    


profile=Button(text='Profile',font=("Times New Roman",18,'bold'),command=prof)
profile.place(x=490,y=165)


def attend():
    # Create a Toplevel window for the attendance system
    attendance_window = tk.Toplevel()
    attendance_window.title("Attendance Manager")
    attendance_window.geometry("600x400")
    
    class AttendanceSystem:
        def __init__(self, root):
            self.root = root
            self.root.title("Attendance Manager")
            self.root.geometry("600x400")

            # Database connection
            self.connection = pymysql.connect(host='localhost',
                                            user='root',
                                            password='Lamjung@2056',
                                            database='stddata')
            
            self.create_widgets()



        def create_widgets(self):
            # Frames
            self.top_frame = tk.Frame(self.root)
            self.top_frame.pack(pady=10)

            self.bottom_frame = tk.Frame(self.root)
            self.bottom_frame.pack(pady=10)

            # Labels
            self.date_label = tk.Label(self.top_frame, text="Date:")
            self.date_label.grid(row=0, column=0, padx=5, pady=5)

            # Date entry
            self.date_var = tk.StringVar()
            self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
            self.date_entry = tk.Entry(self.top_frame, textvariable=self.date_var)
            self.date_entry.grid(row=0, column=1, padx=5, pady=5)

            # Buttons
            self.mark_button = tk.Button(self.top_frame, text="Take Attendance", command=self.mark_attendance)
            self.mark_button.grid(row=0, column=2, padx=5, pady=5)

            self.view_button = tk.Button(self.top_frame, text="View Attendance", command=self.view_attendance)
            self.view_button.grid(row=0, column=3, padx=5, pady=5)

            # Attendance record treeview
            self.attendance_tree = ttk.Treeview(self.bottom_frame, columns=("Name", "Status"), show="headings", height=15)
            self.attendance_tree.heading("Name", text="Name")
            self.attendance_tree.heading("Status", text="Status")
            self.attendance_tree.pack()

        def mark_attendance(self):
            date = self.date_var.get()
            if date:
                try:# Fetch student names from the database
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT FullName FROM studentsdata")
                    students = cursor.fetchall()
                    cursor.close()

                    # Insert attendance records into the database
                    cursor = self.connection.cursor()
                    for student in students:
                        status = tk.messagebox.askyesno("Take Attendance", f"Is {student[0]} present?")
                        if status:
                            attendance_status = "Present"
                        else:
                            attendance_status = "Absent"
                        cursor.execute("INSERT INTO attendance (date, name, status) VALUES (%s, %s, %s)",
                                    (date, student[0], attendance_status))
                    self.connection.commit()
                    cursor.close()
                    tk.messagebox.showinfo("Success", "Attendance marked successfully!")
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
            else:
                tk.messagebox.showerror("Error", "Please enter a date.")

        def view_attendance(self):
            date = self.date_var.get()
            if date:
                try:
                    # Fetch attendance records for the given date
                    cursor = self.connection.cursor()
                    cursor.execute("SELECT name, status FROM attendance WHERE date=%s", (date,))
                    attendance_records = cursor.fetchall()
                    cursor.close()

                    # Clear existing records in the treeview
                    for record in self.attendance_tree.get_children():
                        self.attendance_tree.delete(record)

                    # Insert attendance records into the treeview
                    for record in attendance_records:
                        self.attendance_tree.insert("", "end", values=record)
                except Exception as e:
                    tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
            else:
                tk.messagebox.showerror("Error", "Please enter a date.")
    app = AttendanceSystem(attendance_window)


attendence=Button(text='Take Attendence',font=("Times New Roman",18,'bold'),command=attend)
attendence.place(x=600,y=165)

def noty():
    t=Tk()
    t.title('Notice')
    t.geometry('400x500')
    t.config(bg='powder blue')
    noty_text=Label(t, text="Type the notice:",font=("Times New Roman",18,"normal"),fg="black", bg="powder blue")
    noty_text.pack()
    noty_entry=Entry(t, font=("Times New Roman",18,'normal') , width=30)
    noty_entry.pack()
    noty_button=Button(t, text="Submit",font=("Times New Roman",20,'bold'))
    noty_button.place(x=150,y=400)

notice=Button(text='Notice',font=("Times New Roman",18,'bold'),command=noty)
notice.place(x=40,y=213)


def login2():
    t.destroy()        #destroy current page
    import Hajiri      #To move to login page

#Creating logout button 
log_button1=Button(text="Log Out",height=0,width=5,font=('Times New Roman',18,'bold'),bg='#9e9e9e',fg="black",command=login2)
log_button1.place(x=1280,y=700)

t.mainloop()