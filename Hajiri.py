#HAJIRI(Your Attendence Manager)
#Project from Team Alpha


from tkinter import*
from tkinter import messagebox
import pymysql
def clear():
    Entry1.delete(0,END)
    Entry2.delete(0,END)

def login():
    Entry1.get()
    Entry2.get()
    if(Entry1.get()=="" and Entry2.get()==""):
        messagebox.showinfo("","Blank Not Allowed ")
    elif var1.get()==1 and var2.get()==0:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Lamjung@2056')
            my_cursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use stddata'
        my_cursor.execute(query)
        query='select * from studentsdata where username=%s and password=%s'
        my_cursor.execute(query,(Entry1.get(),Entry2.get()))
        row=my_cursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
            clear()
        else:
            messagebox.showinfo('Welcome','Login Sucessfully As Student')
            s.destroy()
            import studentdash
        

    elif var2.get()==1 and var1.get()==0:
        try:
            con1=pymysql.connect(host='localhost',user='root',password='Lamjung@2056')
            my_cursor1=con1.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use tdata'
        my_cursor1.execute(query)
        query='select * from teachersdata where username=%s and password=%s'
        my_cursor1.execute(query,(Entry1.get(),Entry2.get()))
        row1=my_cursor1.fetchone()
        if row1==None:
            messagebox.showerror('Error','Invalid username or password')
            clear()
        else:
            messagebox.showinfo('Welcome','Login Sucessful As Teacher')
            s.destroy()
            import teacherdash
    else:
        ()
s=Tk()
s.title('HAJIRI LOGIN')
s.config(bg="#5c2e8a")
s.geometry("1400x800")

frame= Frame(s, highlightbackground="#AF69EE", highlightthickness=6, width=400, height=490, bd=0,bg='#966FD6')
frame.place(x=920,y=240)


def visible():
    if chk.get()==1:
        Entry2.config(show="")
    else:
        Entry2.config(show="*")

chk=IntVar()
check=Checkbutton(variable=chk,command=visible,bg='#966FD6')
check.place(x=1260,y=520)


    # elif(username=="lucifer" and password==""):
    #     messagebox.showinfo("","You must enter Password")
    # elif(username=="" and password=="7871"):
    #     messagebox.showinfo("","You must enter Username")
    # elif(username=="lucifer" and password=="7871" and var1.get()==1):
    #     #messagebox.showinfo("","login Success As Student")
    #     Entry1.delete(0,END)
    #     Entry2.delete(0,END)
    #     s.destroy()
    #     import studentdash
    # elif(username=="lucifer" and password=="7871" and var2.get()==1):
    #     messagebox.showinfo("","Login Success As Teacher")
    #     Entry1.delete(0,END)
    #     Entry2.delete(0,END)
    #     s.destroy()
    #     import teacherdash
    # elif(username=="lucifer" and password=="7871" and var1.get()==0 and var2.get()==0):
    #     messagebox.showinfo("","One Option Must Be Selected")
    #     Entry1.delete(0,END)
    #     Entry2.delete(0,END)
         
    # else:
    #     messagebox.showinfo("","Incorrect Username and Password")
    #     Entry1.delete(0,END)
    #     Entry2.delete(0,END)

global entry1
global entry2

Label(s, text="Username",font=('Times New Roman',22,'bold'),bg='#966FD6').place(x=940,y=465)
Label(s, text="Password",font=('Times New Roman',22,'bold'),bg='#966FD6').place(x=940,y=515)

Entry1=Entry(s,bd=3,font=('Times New Roman',20,'normal'))
Entry1.place(x=1045,y=460)

Entry2=Entry(s,show='*', bd=3,font=('Times New Roman',20,'normal'))
Entry2.place(x=1045,y=510)

var=IntVar()
C1 = Checkbutton(s , text = "Remember Me", variable = var, onvalue = 1, offvalue = 0, height=1, \
width = 15, bd=2,font=('Times New Roman',16,'normal'),bg='#966FD6')
C1.place(x=1040,y=560)

var1=IntVar()
Choose1 = Checkbutton(s , text = "Student", variable = var1, onvalue = 1, offvalue = 0, height=1, \
width = 10, bd=2,font=('Times New Roman',16,'normal'),bg='#5c2e8a')
Choose1.place(x=920,y=210)

var2=IntVar()
Choose2 = Checkbutton(s , text = "Teacher", variable = var2, onvalue = 1, offvalue = 0, height=1, \
width = 10, bd=2,font=('Times New Roman',16,'normal'),bg='#5c2e8a')
Choose2.place(x=1020,y=210)

def registration():
    s.destroy()
    import registration

signup=Label(s,text="Don't have a login ID?",font=("Times New Roman",20,'normal'),bg='#966FD6').place(x=940,y=675)
reg_button=Button(text="Register",height=0,width=5,font=('Times New Roman',18,'bold'),bg='#966FD6',fg="blue",command=registration).place(x=1130,y=670)

    
from PIL import Image,ImageTk
class_image=Image. open ("/Users/lucifer/Desktop/Alpha/class.png")
resized_class = class_image.resize ((600,400))
converted_class=ImageTk. PhotoImage(resized_class)
class_label=Label(s , image=converted_class,width=700,height=420,bg='#5c2e8a')
class_label.place(x=70,y=300)

profile_image=Image. open ("/Users/lucifer/Desktop/Alpha/profile.png")
resized_profile = profile_image.resize ((180,160))
converted_profile=ImageTk. PhotoImage(resized_profile)
profile_label=Label(s , image=converted_profile,bg='#966FD6')
profile_label.place(x=1040,y=260)

logo_image=Image. open ("/Users/lucifer/Desktop/Alpha/logo2.png")
resized_logo = logo_image.resize ((200,130))
converted_logo=ImageTk. PhotoImage(resized_logo)
logo_label=Label(s , image=converted_logo,width=200,height=160,bg='#5c2e8a')
logo_label.place(x=320,y=10)


title=Label(s,text='HAJIRI',font=('Times New Roman',110,'bold','underline'),bg='#5c2e8a',fg='#FFF192')
title.place(x=225,y=153)
slogan=Label(s,text='Your Attendance Manager',font=('Times New Roman',20,'normal'),bg='#5c2e8a',fg='#FFF192')
slogan.place(x=297,y=260)
login_button=Button(text="login" ,command=login,height=1,width=8,font=('Times New Roman',30,'bold'),bg='#5c2e8a')
login_button.place(x=1060,y=605)

s.mainloop()