
from tkinter import*
t=Tk()

t.title('Students Dashboarrd')
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
    t=Tk()
    t.title('Attendence Records')
    t.geometry('800x580')
    t.config(bg='powder blue')

attendence=Button(text='Take Attendence',font=("Times New Roman",18,'bold'),command=attend)
attendence.place(x=600,y=165)

def noty():
    t=Tk()
    t.title('')
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
    t.destroy()
    import Hajiri
log_button1=Button(text="Log Out",height=0,width=5,font=('Times New Roman',18,'bold'),bg='#9e9e9e',fg="black",command=login2)
log_button1.place(x=1280,y=700)

t.mainloop()