# from tkinter import *
# win=Tk()
# win.title("kehar")
# win.iconbitmap("keh.ico")
# win.maxsize(width=900,height=800)
# # win.minsize(width=200,height=100)
# win.geometry("600x300")
# win.mainloop()


# from tkinter import *
# root=Tk()
# root.bg="green"
# root.mainloop()



# from tkinter import *
# from turtle import right
# root=Tk()
# redbutton=Button(root,text="LEFT",fg="green")
# redbutton.pack(side=LEFT)
# greenbutton=Button(root,text="right",fg="black")
# greenbutton.pack(side=RIGHT)
# bluebutton=Button(root,text="TOP",fg='blue')
# bluebutton.pack(side=TOP)
# blackbutton=Button(root,text="BOTTOM",fg="red")
# blackbutton.pack(side=BOTTOM)
# root.mainloop()


# from tkinter import *
# root=Tk()
# name=Label(root,text="Name").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# password=Label(root,text="Password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# submit=Button(root,text="submit").grid(row=4,column=1)
# root.mainloop()


# from tkinter import *
# top=Tk("480x250")
# name=Label(top,text="Name",fg="Green").place(x=30,y=50)
# adress=Label(top,text="Adress",fg="Yellow").place(x=30,y=90)
# contact=Label(top,text="Contact",fg="Red").place(x=30,y=130)
# top.configure(bg="Grey")
# e1=Entry(top).place(x=80,y=50,)
# e2=Entry(top).place(x=80,y=50)
# e3=Entry(top).place(x=95,y=130)
# top.mainloop()


# from tkinter import *
# a=Tk("400x250")
# name=Label(text="Python").place(x=570,y=320)
# button=Button(text="Button").place(x=570,y=360)
# a.mainloop()


# from cProfile import label
# from curses import window
# from tkinter import *
# a=Tk("720x1080")
# b=Label(a,text="Username",fg="green",font=20).place(x=30,y=50)
# c=Label(a,text="Email",fg="green",font=20).place(x=30,y=90)
# d=Label(a,text="Age",fg="green",font=20).place(x=30,y=130)
# e=Label(a,text="Date of Birth",fg="green",font=20).place(x=30,y=170)
# f=Label(a,text="Password",fg="green",font=20).place(x=30,y=210)
# g=Label(a,text="Confirm Password",fg="green",font=20).place(x=30,y=250)
# h=Button(a,text="Signup",font=150).place(x=150,y=300)
# a.configure(bg="gray")
# a1=Entry(a,font=15).place(x=140,y=50)
# a2=Entry(a,font=15).place(x=100,y=90)
# a3=Entry(a,font=15).place(x=90,y=130)
# a4=Entry(a,font=15).place(x=169,y=170)
# a5=Entry(a,font=15).place(x=140,y=210)
# a6=Entry(a,font=15).place(x=210,y=250)
# a.mainloop()

# root=Tk()
# root.title("GUI")
# myLabel=Label(root,text="Tkinter",fg="grey",font="Arial")
# myLabel.pack()
# root.mainloop()


# a=Tk()
# a.title("Login")
# b=Label(a,text="Username").place(x=30,y=50)
# c=Label(a,text="password").place(x=30,y=90)
# d=Button(a,text="Login").place(x=30,y=150)
# e=Button(a,text="signup").place(x=130,y=150)
# a1=Entry(a,font=15).place(x=140,y=50)
# a2=Entry(a,font=15).place(x=100,y=90)
# a.mainloop()

# from cgitb import text
# from curses import window
# from tkinter import *
# window=Tk()
# window.maxsize(width=300,height=300)
# window.minsize(width=300,height=300)
# def func():
#     print("Button is clicked")
# btn=Button(window,text="Login",command=func)
# btn.pack(side="top")
# window.mainloop()


# window=Tk()
# def myclick():
#     mylabel=Label(window,text="look i clicked a button",fg="red",bg="black",font=50)
#     mylabel.pack()

# my_button=Button(window,text="Click me",padx=10,pady=10,command=myclick,fg="click",bg="black")
# my_button.pack()
# window.mainloop()

# a=Button(text="Button",font=70,state=DISABLED).place(x=30,y=50)
# b=Button(text="Button",font=70).place(x=30,y=90)
# c=Button(text="Button",font=70).place(x=30,y=150)
# d=Button(text="Button",font=70).place(x=30,y=190)
# window.mainloop()



# e=Entry(window,width=50,bg="blue",fg="White",borderwidth=5,font=20)
# e.pack()

# def myclick():
#     myLabel=Label(window,text="Hello"+e.get())
#     myLabel.pack()
# btn=Button(window,text='Click me',padx=10,pady=10,command=myclick)
# btn.pack()
# window.mainloop()

# root=Tk()
# root.title("GUI")
# root.maxsize(width=600,height=300)
# root.minsize(width=600,height=300)
# def add():
#     x=var.get()
#     print(x)
#     mylabell.config(text=x,bg="green")
# mylabel=Label(root,text="User Name",fg="red",bg="yellow")
# mylabel.place(x=10,y=10)

# mylabell=Label(root,text="Nothing",fg="red",bg="yellow")
# mylabell.place(x=40,y=120)

# var=StringVar()
# ent=Entry(root,bg="white",fg="black",textvariable=var)
# ent.place(x=80,y=10)

# btn=Button(root,text="Submit",bg="green",fg="white",command=add)
# btn.place(x=20,y=80)
# root.mainloop() 


# root=Tk()
# def click():
#     text1="Address:"+mytext.get("1.0",END)
#     lbl.config(text=str(text1))

# mytext=Text(root,font=20,width=20,height=10)
# mytext.place(x=0,y=50)

# btn=Button(root,text="Click Me",font=30,command=click)
# btn.place(x=400,y=300)

# lbl=Label(root,text="",font=30)
# lbl.place(x=200,y=300)
# root.mainloop()



# from tkinter import *
# window=Tk()
# frame=LabelFrame(window,text="this is my frame",padx=10,pady=10)
# frame.pack(padx=50,pady=50)
# b=Button(frame,text="Dont click here")
# b2=Button(frame,text=".....here")
# b.grid(row=0,column=0)
# b2.grid(row=1,column=1)
# window.mainloop()


# from tkinter import *
# window=Tk()
# def add():
#     print(var.get())
# var=IntVar()
# r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
# r2.pack(anchor=W)
# window.mainloop()



# from tkinter import*
# window=Tk()
# def add():
#     if var.get()==1:
#         print("Male")
#     else:
#         print("Female")
# var=IntVar()
# r1=Radiobutton(window,text="Male",variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="Female",variable=var,value=2,command=add)
# r2.pack(anchor=W)
# window.mainloop()
# from tkinter import*
# window=Tk()
# def add():
#     selection="you have selected the option"+ str(var.get())
#     lable.config(text=selection)
# var=IntVar()
# r1=Radiobutton(window,text='option1',variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2=Radiobutton(window,text="option2",variable=var,value=2,command=add)
# r2.pack(anchor=W)
# r3=Radiobutton(window,text="option3",variable=var,value=3,command=add)
# r3.pack(anchor=W)
# lable=Label(window)
# lable.pack()
# window.mainloop()


# from curses import window
# from logging import root
# from tkinter import *
# top=Tk()
# def add():
#     label.config(text=CheckVar1.get())
# CheckVar1=IntVar()

# C1=Checkbutton(top,text="Music",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
# C1.pack()
# btn=Button(top,text="Click",command=add)
# label=Label(top,text="")
# label.pack()
# btn.pack()
# top.mainloop()

# from PIL import Image,ImageTk
# window=Tk()
# window.title("LOGIN")
# my_image=ImageTk.PhotoImage(Image.open("ronaldoo.png"))
# my_label=Label(image=my_image)
# my_label.pack()

# button_quit=Button(window,text="Exit",command=window.quit,width=20)
# button_quit.pack()
# window.mainloop()


# from PIL import Image, ImageTk
# window=Tk()
# window.title("LOGIN")
# my_image=Image.open("ronaldo.jpg")
# resized_image=my_image.resize((300,250))
# converted_image=ImageTk.PhotoImage(resized_image)
# mylabel=Label(window,image=converted_image)
# mylabel.pack()
# window.mainloop()


# from tkinter import messagebox
# root=Tk()
# def popup():
#     messagebox.showinfo("This is my popup","hello world")
# btn=Button(root,text="popup",command=popup).pack()
# root.mainloop()


# from tkinter import messagebox
# from urllib import response
# root=Tk()
# def popup():
#     response=messagebox.askyesno("this is my popup","hello world")
#     Label(root,text=response).pack()

#     if response==1:
#         Label(root,text="clicked yes").pack()
#     else:
#         Label(root,text="clicked no").pack()

# btn=Button(root,text="popup",command=popup).pack()
# root.mainloop()



# from tkinter import*
# from PIL import Image, ImageTk
# root=Tk()
# def open():
#     global my_img
#     top=Toplevel()
#     my_img=ImageTk.PhotoImage(Image.open("messiuu.png"))
#     my_label=Label(top,image=my_img)
#     btn=Button(top,text="close window",command=top.destroy)
#     btn.pack()
# btnn=Button(root,text="open",command=open)
# btnn.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("200x200")
# def show():
#     Label.config(text=clicked.get())
# options=[
#     "Ram",
#     "hari",
#     "Sita",
#     "Gita"
# ]
# clicked=StringVar()
# clicked.set("Ram")
# drop=OptionMenu(root,clicked,*options)
# drop.pack()
# button=Button(root,text="clicked Me",command=show).pack()
# label=Label(root,text="")
# label.pack()
# root.mainloop()