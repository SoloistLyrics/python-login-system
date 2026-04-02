# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:00:23 2026
@author: WINDOWS 10
"""
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def SignIn():
    username=user.get()
    password=code.get()
    
    if username== 'admin' and password== '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        
        Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold' )).pack(expand=True)
        
        screen.mainloop()
        
    elif username!="admin" and password!='1234':
        messagebox.showerror("Invalid", "invalid username and password")
    elif password!="1234":
        messagebox.showerror("Invalid", "invalid password")
    elif username!='admin':
        messagebox.showerror("Invalid", "invalid username")
        
        
        
        
# ✅ Image resized to be taller and closer to the frame
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'login.jpg')
img = ImageTk.PhotoImage(Image.open(img_path).resize((420, 400)))  # ✅ Resized here
Label(root, image=img, bg='white').place(x=40, y=50)               # ✅ Repositioned

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

##########------------------------------------------------------

def  OnEnter(e):
    user.delete(0, 'end')
    
def OnLeave(e):
    name=user.get()
    if name== '':
        user.insert(0, 'Username')
        
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', OnEnter)
user.bind('<FocusOut>', OnLeave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

##########------------------------------------------------------

def  OnEnter(e):
    code.delete(0, 'end')
    
def OnLeave(e):
    name=code.get()
    if name== '':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', OnEnter)
code.bind('<FocusOut>', OnLeave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#############################################################

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=SignIn).place(x=35,y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

SignUp = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
SignUp.place(x=215, y=270)


root.mainloop()