# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:31:19 2022

@author: KAIZEN
"""


import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import os
from PIL import ImageTk, Image



class CreateAssessment(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='right', fill='both', expand=True)
        
        
        
        session_frame = tk.LabelFrame(self)
        session_frame.pack(side='left')
        
        # Create session dropdown menu 
        self.session_select = tk.StringVar()
        session_dropdown_list = ["Select session"] 
         # Get list of sessions from database
        #db_fetch_session_list = [session[1] for session in db.fetch_session()]
         # Concatenate both lists 
        #session_dropdown_list += db_fetch_session_list
        session_dropdown_menu = ttk.OptionMenu(session_frame, self.session_select, *session_dropdown_list)
        session_dropdown_menu.grid(row=0, column=3, pady=10, padx=5)
        
        # Create term dropdown menu 
        self.term_select = tk.StringVar()
        self.term_dropdown_list = ["Select term", "1", "2", "3"]
        term_dropdown_menu = ttk.OptionMenu(session_frame, self.term_select, *self.term_dropdown_list)
        term_dropdown_menu.grid(row=0, column=3, pady=10, padx=5)
        
        assessment_frame = tk.LabelFrame(self)
        assessment_frame.pack(side='left')
        
        student_name = tk.Label(assessment_frame, text=self.treeview.blahblah.get())
        student_name.grid(row=0, column=1)
        
        student_class = tk.Label(assessment_frame, text=self.treeview.blahblah.get())
        student_class.grid(row=1, column=1)
        
        # Create assessment type dropdown menu 
        self.assesssment_select = tk.StringVar()
        self.assesssment_list = ["Select assessment"]
        assessment_dropdown_menu = ttk.OptionMenu(session_frame, self.term_select, *self.term_dropdown_list)
        assessment_dropdown_menu.grid(row=3, column=3, pady=20, padx=10)
        
        # Add Buttons # Will make much smaller. Perhaps with an icon on the button rather than words. Icon-ed may still need label beside it tho
        add_button = ttk.Button(assessment_frame, text="Add Pic", command=lambda: self.add_profile_picture(), width=42)
        add_button.grid(row=2, column=1, padx=10, pady=5, )
        
        
    def add_profile_picture(self):    
        filename = filedialog.askopenfilename(
            initialdir = "C:/Documents",
            title = "Open A File",
            filetype = (("jpeg files", "*.jpg"), ("png files", "*.png"))
            )
        if filename:
            try:
                filename = r"{}".format(filename)
                self.img = Image.open(filename)
                self.img = self.img.resize((1258,548))
                # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
                self.img = ImageTk.PhotoImage(self.img, master=self.assesment_frame)
                
            except(ValueError):
                messagebox.showerror("File Error", "File could not be opened... try again!")
            except FileNotFoundError:
                messagebox.showerror("File Error", "File could not be found... try again!")
                
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1260, height=550)
        self.my_canvas.grid(row=0, column = 0, rowspan=2, pady=5, padx=10)
        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')        



class AssessmentTreeview(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='right', fill='both', expand=True)
        
        