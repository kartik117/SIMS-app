# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:11:04 2021

@author: KAIZEN
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import ImageTk, Image

from dashboard import Dashboard

from db_srms_sqlite import Database
db = Database('new_single_user3.db')

class SRMSApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, *kwargs)
        tk.Tk.wm_title(self, 'School Records Management System')
        #tk.Tk.iconbitmap(self, default='png-to-ico.ico')
        tk.Tk.geometry(self, '1360x750')
        #tk.Tk.resizable(self, width= False, height = False)
        
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (StartPage, SignUp, Login, Dashboard):
            frame = page(parent=container, controller=self)
          
            self.frames[page] = frame
    
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        # Add menu bar of frame
        menubar = frame.menubar(self)
        self.configure(menu=menubar)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("images/lib1.jpg")
        self.img = self.img.resize((1358,748))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)

        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1360, height=750)
        self.my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        self.my_canvas.create_text(180, 250, text = 'SRMS 1.0', font=("Arial black", 40, 'bold italic'), fill='white')
        self.my_canvas.create_text(120, 285, text = 'All your records at the touch of a button.', font=("Arial black", 10), fill='white', anchor='nw')

        # Add buttons
        login_button = ttk.Button(self, text = 'Login', width = 25, command=lambda: controller.show_frame(Login))
        register_button = ttk.Button(self, text = 'Register', width = 25, command=lambda: controller.show_frame(SignUp))
        # Button windows
        login_button_window = self.my_canvas.create_window(500, 350, anchor= 'nw', window=login_button)
        register_button_window = self.my_canvas.create_window(750, 350, anchor= 'nw', window=register_button)

        '''
        # Binding
        self.bind('<Configure>', self.resizer)

    def resizer(self, e):
        # Open our image
        self.bg1 = Image.open("pexels-olenka-sergienko-3646172.jpg")
        # Resize the image
        self.resized_bg = self.bg1.resize((e.width, e.height), Image.ANTIALIAS)
        # Define our image again
        self.new_img = ImageTk.PhotoImage(self.resized_bg)
        # Add it back to the canvas
        self.my_canvas.create_image(0,0, image=self.new_img, anchor='nw')
        # Add text back
        self.my_canvas.create_text(180, 330, text = 'SRMS 1.0', font=("Arial black", 40, 'bold italic'), fill='white')

        '''

    def menubar(self, root):
        menubar = tk.Menu(root)
        return(menubar)

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("images/lib2.jpg")
        self.img = self.img.resize((1358,748))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1360, height=750)
        self.my_canvas.grid(row=0, column = 0)
        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')
        # Add label
        self.my_canvas.create_text(450, 208, text = 'Enter your username or ID.', font=("Arial black", 12, 'italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 278, text = 'Enter your password.', font=("Arial black", 12, 'italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 348, text = 'Retype password.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')

        # Variables
        self.temp_username = tk.StringVar()
        self.temp_password = tk.StringVar()
        self.temp_confirm_password = tk.StringVar()
       # Add entry
        self.username_entry = tk.Entry(self, textvariable=self.temp_username, font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.password_entry = tk.Entry(self, textvariable=self.temp_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.confirm_password_entry = tk.Entry(self, textvariable=self.temp_confirm_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)

        # Buttons
        sign_up_button=tk.Button(self, text='CREATE ACCOUNT', font=('Calibri', 12, 'bold'), width=48, height=2,
                          command=self.register)
        login_button=ttk.Button(self, text='Login', width=20,
                          command=lambda: controller.show_frame(Login))
        back_to_home_button=ttk.Button(self, text='Back to Home', width=20,
                          command=lambda: controller.show_frame(StartPage))

        # Create button windows
        username_entry_window = self.my_canvas.create_window(450, 230, anchor= 'nw', window=self.username_entry)
        pw_entry_window = self.my_canvas.create_window(450, 300, anchor= 'nw', window=self.password_entry)
        confirm_pw_entry_window = self.my_canvas.create_window(450, 370, anchor= 'nw', window=self.confirm_password_entry)
        sign_up_button_window = self.my_canvas.create_window(450, 440, anchor= 'nw', window=sign_up_button)
        login_button_window = self.my_canvas.create_window(1000, 50, anchor= 'nw', window=login_button)
        back_to_home_button_window = self.my_canvas.create_window(1150, 50, anchor= 'nw', window=back_to_home_button)


    def register(self):
        # Validation
        if self.temp_password.get() != self.temp_confirm_password.get():
            messagebox.showerror('Password Error', 'Your passwords do not match.')
            return

        list_of_files = os.listdir()
        if 'single user' not in list_of_files:
            username_info = self.temp_username.get()
            password_info = self.temp_password.get()

            file = open('single user', 'w')
            file.write(username_info+'\n')
            file.write(password_info)
            file.close()

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)

            label5 = tk.Label(self, text = "Registration successful.\nClick login to log into your account", fg = "green", font = ("Calibri", 11))
            label5.grid(row=9, padx=10, sticky=tk.W)
        else:
            label5 = tk.Label(self, text = "Registration unsuccessful.\n(Single User App)", fg = "red", font = ("Calibri", 11))
            label5.grid(row=9,padx=10, sticky=tk.W)

    def menubar(self, root):
        menubar = tk.Menu(root)
        return(menubar)

class Login(tk.Frame):
    login_name = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Image import
        self.img = Image.open("images/lib3.jpg")
        self.img = self.img.resize((1358,748))
        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1360, height=750)
        self.my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        self.my_canvas.create_text(450, 208, text = 'Enter your username or ID.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 278, text = 'Enter your password.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')

        # Variables
        self.temp_login_name = tk.StringVar()
        self.temp_login_password = tk.StringVar()
        self.login_name = ''
        self.login_attempt = 0

        # Add entry
        self.username_entry1 = tk.Entry(self, textvariable=self.temp_login_name, font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.password_entry1 = tk.Entry(self, textvariable=self.temp_login_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)

        # Buttons
        login_button = tk.Button(self, text = 'SIGN IN', font=('Calibri', 12, 'bold'), width=48, height=2,
                            command= lambda : controller.show_frame(Dashboard) if self.verify_login() == 1 else messagebox.showerror('', 'Login Unsuccessful.'))#self.verify_login)
        login_button.bind("<Return>", self.login_check)
        back_to_home_button=ttk.Button(self, text='Back to Home', width=20,
                          command=lambda: controller.show_frame(StartPage))
        sign_up_button=ttk.Button(self, text='Sign Up', width=20,
                          command=lambda: controller.show_frame(SignUp))

        # Create button windows
        username_entry_window = self.my_canvas.create_window(450, 230, anchor= 'nw', window=self.username_entry1)
        pw_entry_window = self.my_canvas.create_window(450, 300, anchor= 'nw', window=self.password_entry1)
        login_button_window = self.my_canvas.create_window(450, 400, anchor= 'nw', window=login_button)
        sign_up_button_window = self.my_canvas.create_window(1000, 50, anchor= 'nw', window=sign_up_button)
        back_to_home_button_window = self.my_canvas.create_window(1150, 50, anchor= 'nw', window=back_to_home_button)

    
    def verify_login(self):
        # check if login username entry matches username and if login password entry matches password
        with open("single user", "r") as file:
            file_data = file.read()

        file_data = file_data.split('\n')

        # Validation
        if self.temp_login_name.get() == file_data[0]:
            if self.temp_login_password.get() == file_data[1]:
                self.login_attempt = 1
                # clear user's entries from input bar after login button is clicked
                self.clear_entry()
            else:
                messagebox.showerror('Password Error', 'Incorrect password.')
                # clear user's entries from input bar after message popup button is clicked
                self.clear_entry()
                return
        elif self.temp_login_name.get() == file_data[2]:
            if self.temp_login_password.get() == file_data[3]:
               self.login_attempt = 2
               # clear user's entries from input bar after login button is clicked
               # self.clear_entry()
            else:
                messagebox.showerror('Password Error', 'Incorrect password.')
                # clear user's entries from input bar after message popup button is clicked
                self.clear_entry()
                return
        else:
            self.login_attempt = 0
            #messagebox.showerror('Account Error', 'No account found!')
        return self.login_attempt

    def clear_entry(self):
        self.username_entry1.delete(0, tk.END)
        self.password_entry1.delete(0, tk.END)
    
    def login_check(self, event):
        if self.verify_login() == 1:
            self.controller.show_frame(Dashboard)
        else:
            messagebox.showerror('', 'Login Unsuccessful.')
    
    def menubar(self, root):
        menubar = tk.Menu(root)
        return(menubar)
    
    

app = SRMSApp()
app.mainloop()
