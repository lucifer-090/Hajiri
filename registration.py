
from tkinter import*
from tkinter import messagebox
import pymysql

def clear():
    name_ent.delete(0,END)
    add_ent.delete(0,END)
    user_ent.delete(0,END)
    pass_ent.delete(0,END)
    cont_ent.delete(0,END)

def connect_database():
    if name_ent.get()=="" or add_ent.get()=="" or user_ent.get()=="" or pass_ent.get()=="" or cont_ent.get()=="":
        messagebox.showerror('Error',"All fields Are Required")
    elif std_var.get()==0 and tech_var.get()==0:
        messagebox.showerror('Error',"One Option Must Be Selected")
    elif std_var.get()==1 and tech_var.get()==0:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Lamjung@2056')
            my_cursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database connectivity Issue,Please Try Again")
            return

        try:
            query="create database stddata"
            my_cursor.execute(query)
            query="use stddata"
            my_cursor.execute(query)
            query="create table studentsdata(ID int auto_increment primary key not null, FullName varchar(100), address varchar(100), username varchar(50), password varchar(20), contact varchar(10)) "
            my_cursor.execute(query)
        except:
            my_cursor.execute('use stddata')

        query="insert into studentsdata(FullName,address,username,password,contact) values(%s,%s,%s,%s,%s) "
        my_cursor.execute(query,(name_ent.get(),add_ent.get(),user_ent.get(),pass_ent.get(),cont_ent.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is Successful')
        clear()
        r.destroy()
        import Hajiri
    elif tech_var.get()==1 and std_var.get()==0:
        try:
            con1=pymysql.connect(host='localhost',user='root',password='Lamjung@2056')
            my_cursor1=con1.cursor()
        except:
            messagebox.showerror('Error',"Database connectivity Issue,Please Try Again")
            return

        try:
            query="create database tdata"
            my_cursor1.execute(query)
            query="use tdata"
            my_cursor1.execute(query)
            query="create table teachersdata(ID int auto_increment primary key not null, FullName varchar(100), address varchar(100), username varchar(50), password varchar(20), contact varchar(10)) "
            my_cursor1.execute(query)
        except:
            my_cursor1.execute('use tdata')

        query="insert into teachersdata(FullName,address,username,password,contact) values(%s,%s,%s,%s,%s) "
        my_cursor1.execute(query,(name_ent.get(),add_ent.get(),user_ent.get(),pass_ent.get(),cont_ent.get()))
        con1.commit()
        con1.close()
        messagebox.showinfo('Success','Registration is Successful')
        clear()
        r.destroy()
        import Hajiri
    else:
        ()
        



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
        pass_ent.config(show="")
    else:
        pass_ent.config(show="*")

chk=IntVar()
check=Checkbutton(variable=chk,command=visible,bg='#966FD6')
check.place(x=450,y=405)

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



name_ent=Entry(r,font=('Times New Roman',20,'normal'))
name_ent.place(x=230,y=230)
add_ent=Entry(r,font=('Times New Roman',20,'normal'))
add_ent.place(x=230,y=285)
user_ent=Entry(r,font=('Times New Roman',20,'normal'))
user_ent.place(x=230,y=340)
pass_ent=Entry(r,show='*',font=('Times New Roman',20,'normal'))
pass_ent.place(x=230,y=395)
cont_ent=Entry(r,font=('Times New Roman',20,'normal'))
cont_ent.place(x=230,y=450)

reg_button=Button(text='REGISTER',font=("Times New Roman",28,'bold'),command=connect_database)
reg_button.place(x=185,y=580)

r.mainloop()