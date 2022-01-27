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
        
        
        
        sess_assess_frame = tk.Frame(self) # wraps around session and assessment frames to keep them aligned
        sess_assess_frame.pack(side='left', fill='both', pady=26, padx=15)
        
        session_frame = tk.LabelFrame(sess_assess_frame)
        session_frame.pack(side='top', fill='x', anchor=tk.N)
        
        # Create session dropdown menu
        session_label = tk.Label(session_frame, text="Academic Year")
        session_label.grid(row=0,column=0, padx=5, sticky='W')
        self.session_select = tk.StringVar()
        session_dropdown_list = ["Select session"] 
         # Get list of sessions from database
        #db_fetch_session_list = [session[1] for session in db.fetch_session()]
         # Concatenate both lists 
        #session_dropdown_list += db_fetch_session_list
        session_dropdown_menu = ttk.OptionMenu(session_frame, self.session_select, *session_dropdown_list)
        session_dropdown_menu.grid(row=1, column=0, pady=(5,30), padx=5)
        
        # Create term dropdown menu
        term_label=tk.Label(session_frame, text="Term")
        term_label.grid(row=2, column=0, pady=(20,0), padx=5, sticky='W')
        self.term_select = tk.StringVar()
        self.term_dropdown_list = ["Select term", "1", "2", "3"]
        term_dropdown_menu = ttk.OptionMenu(session_frame, self.term_select, *self.term_dropdown_list)
        term_dropdown_menu.grid(row=3, column=0, pady=(5,80), padx=5)
        
        assessment_frame = tk.LabelFrame(sess_assess_frame)
        assessment_frame.pack(side='bottom',fill='both', expand=True)
        
        '''
        student_name = tk.Label(assessment_frame, text=self.treeview.blahblah.get())
        student_name.grid(row=0, column=1)
        
        student_class = tk.Label(assessment_frame, text=self.treeview.blahblah.get())
        student_class.grid(row=1, column=1)
        '''
        # Create assessment type dropdown menu
        assessment_label = tk.Label(assessment_frame, text="Assessment type")
        assessment_label.grid(row=3, column=0, columnspan=2, pady=(40, 20), padx=5, sticky='W')
        self.assessment_select = tk.StringVar()
        self.assessment_list = ["Select assessment"]
        assessment_dropdown_menu = ttk.OptionMenu(assessment_frame, self.assessment_select, *self.assessment_list)
        assessment_dropdown_menu.grid(row=4, column=0, columnspan=2, pady=5, padx=5)
        
        self.assessment_select1 = tk.StringVar()
        self.assessment_list1 = ["Select assessment"]
        assessment_dropdown_menu1 = ttk.OptionMenu(assessment_frame, self.assessment_select1, *self.assessment_list1)
        assessment_dropdown_menu1.grid(row=5, column=0, columnspan=2, pady=5, padx=5)
        
        self.assessment_select2 = tk.StringVar()
        self.assessment_list2 = ["Select assessment"]
        assessment_dropdown_menu2 = ttk.OptionMenu(assessment_frame, self.assessment_select2, *self.assessment_list2)
        assessment_dropdown_menu2.grid(row=6, column=0, columnspan=2, pady=5, padx=5)
        
        score= tk.Label(assessment_frame, text="Score")
        score.grid(row=3, column=3, padx=20, pady=(40, 20))
        score_box = tk.Entry(assessment_frame, text=score, width=15)
        score_box.grid(row=4, column=3, padx=20)
        
        # Add photo # Will make much smaller. Perhaps with an icon on the button rather than words. Icon-ed may still need label beside it tho
        add_photo_button = ttk.Button(assessment_frame, text="Add Photo", command=lambda: self.add_profile_picture(), width=15)
        add_photo_button.grid(row=2, column=3, padx=10, pady=20)
        
        
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
                self.img = self.img.resize((58,48))
                # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
                self.img = ImageTk.PhotoImage(self.img, master=self)
                
            except(ValueError):
                messagebox.showerror("File Error", "File could not be opened... try again!")
            except FileNotFoundError:
                messagebox.showerror("File Error", "File could not be found... try again!")
                
        # Define canvas
        self.my_canvas = tk.Canvas(self.assessment_frame, width=60, height=50)
        self.my_canvas.grid(row=0, column = 0, rowspan=2, pady=5, padx=10)
        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')        



class AssessmentTreeview(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='right', fill='both', expand=True)
        
        