
import tkinter as tk
from tkinter import*
h=tk.Tk()
import pymysql
from tkinter import messagebox

def prof():
    h=Tk()
    h.title('Your Profile')
    h.geometry('400x480')
    h.config(bg='powder blue')
    try:
        con=pymysql.connect(host='localhost',user='root',password='Lamjung@2056')
        my_cursor=con.cursor()

    except:
        messagebox.showerror('Error','Connection is not established try again')
        return
    
    query='use stddata'
    my_cursor.execute(query)
    query='select * from studentsdata'
    my_cursor.execute(query)
    ro=my_cursor.fetchall()
    print_ro=''
   
    
    for row in ro:
          print_ro += str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])
    query_label=Label(h, text=ro)
    query_label.place(x=20,y=50)
    con.close()
            

        

    
       

    




profile=Button(text='Profile',font=("Times New Roman",18,'bold'),command=prof)
profile.place(x=490,y=165)

def attend():
    h=Tk()
    h.title('Your Attendence Records')
    h.geometry('800x580')
    h.config(bg='powder blue')
   
attendence=Button(text='Attendence Records',font=("Times New Roman",18,'bold'),command=attend)
attendence.place(x=600,y=165)

tic=Button(text='Tickets',font=("Times New Roman",18,'bold'))
tic.place(x=815,y=165)

def noty():
    h=Tk()
    h.title('')
    h.geometry('400x480')
    h.config(bg='powder blue')

noti=Button(text='Notice',font=("Times New Roman",18,'bold'),command=noty)
noti.place(x=40,y=213)

h.title('Students Dashboarrd')
h.geometry("1400x800")
h.config(bg='#02bbd4')


from PIL import Image,ImageTk
std_dash=Image. open ("/Users/lucifer/Desktop/Alpha/std dash.jpg")
resized_std = std_dash.resize ((380,200))
converted_std=ImageTk. PhotoImage(resized_std)
std_label=Label(h , image=converted_std,width=380,height=200,bg='#02bbd4')
std_label.place(x=30,y=10)

std_class=Image. open ("/Users/lucifer/Desktop/Alpha/classroom1.jpg")
resized_class = std_class.resize ((880,500))
converted_class=ImageTk. PhotoImage(resized_class)
class_label=Label(h , image=converted_class,width=880,height=500,bg='#02bbd4')
class_label.place(x=260,y=250)

line=Frame(h, bg='black',height=3,width=1300)
line.place(x=40,y=205)

def login1():
    h.destroy()
    import Hajiri

log_button1=Button(text="Log Out",height=0,width=5,font=('Times New Roman',18,'bold'),bg='#02bbd4',fg="black",command=login1)
log_button1.place(x=1280,y=700)


h.mainloop()



