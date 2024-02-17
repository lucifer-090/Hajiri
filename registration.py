
from tkinter import*
r=Tk()
r.title('HAJIRI REGISTRATION')
r.geometry("1400x800")
r.config(bg='#5c2e8a')


from PIL import Image,ImageTk
reg_image=Image. open ("/Users/lucifer/Desktop/Alpha/reg title.jpg")
resized_logo = reg_image.resize ((980,730))
converted_logo=ImageTk. PhotoImage(resized_logo)
reg_label=Label(r ,image=converted_logo,width=980,height=730,bg='#5c2e8a')
reg_label.place(x=360,y=10)

sign_up=Image. open ("/Users/lucifer/Desktop/Alpha/sign up.png")
resized_sign = sign_up.resize ((340,75))
converted_img=ImageTk. PhotoImage(resized_sign)
sign_label=Label(r ,image=converted_img,width=340,height=75,bg='#5c2e8a')
sign_label.place(x=60,y=0)


frame= Frame(r, highlightbackground="#AF69EE", highlightthickness=6, width=510, height=650, bd=0,bg='#966FD6')
frame.place(x=40,y=75)

fill=Label(r, text="Fill Your Details",font=("Lucida Calligraphy",26,'bold','underline'),bg='#966FD6',fg="black")
fill.place(x=60,y=110)


def visible():
    if chk.get()==1:
        e4.config(show="")
    else:
        e4.config(show="*")

chk=IntVar()
check=Checkbutton(variable=chk,command=visible,bg='#966FD6')
check.place(x=450,y=350)

def login():
    r.destroy()
    import Hajiri

log=Label(r ,text="Already have a login ID?",font=("Times New Roman",22,'normal'),bg='#966FD6').place(x=60,y=655)
log_button=Button(text="Login",height=0,width=3,font=('Times New Roman',18,'bold'),bg='#966FD6',fg="blue",command=login)
log_button.place(x=290,y=655)

std_var=IntVar()
std_button = Checkbutton(r , text = "Student", variable = std_var, onvalue = 1, offvalue = 0, height=1, \
width = 9, bd=3,font=('Times New Roman',22,'normal','underline'),fg="black",bg='#966FD6')
std_button.place(x=230,y=170)

tech_var=IntVar()
tech_button = Checkbutton(r , text = "Teacher", variable = tech_var, onvalue = 1, offvalue = 0, height=1, \
width = 9, bd=3,font=('Times New Roman',22,'normal','underline'),fg="black",bg='#966FD6')
tech_button.place(x=340,y=170)

Deg=Label(text="DEGISNATION",font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=175)
name=Label(text='FULL NAME',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=230)
address=Label(text='ADDRESS',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=285)
login_id=Label(text='USERNAME',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=340)
password=Label(text='PASSWORD',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=395)
contact=Label(text='CONTACT',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=450)
DOB=Label(text='DATE OF BIRTH',font=('Times New Roman',18,'bold'),bg='#966FD6').place(x=60,y=505)


e1=Entry(r,font=('Times New Roman',20,'normal'))
e1.place(x=230,y=230)
e2=Entry(r,font=('Times New Roman',20,'normal'))
e2.place(x=230,y=285)
e3=Entry(r,font=('Times New Roman',20,'normal'))
e3.place(x=230,y=340)
e4=Entry(r,show='*',font=('Times New Roman',20,'normal'))
e4.place(x=230,y=395)
e5=Entry(r,font=('Times New Roman',20,'normal'))
e5.place(x=230,y=450)
e6=Entry(r,font=('Times New Roman',20,'normal'))
e6.place(x=230,y=505)


reg_button=Button(text='REGISTER',font=("Times New Roman",28,'bold'))
reg_button.place(x=185,y=580)

r.mainloop()