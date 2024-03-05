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

#Checkbutton
chk=IntVar()
check=Checkbutton(variable=chk,command=visible,bg='#966FD6')
check.place(x=1260,y=520)


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

s.mainloop()