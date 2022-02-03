# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:55:41 2022

@author: KAIZEN
"""


import tkinter as tk
from tkinter import ttk



from assessments import CreateAssessment, AssessmentTreeview



class NavBarAssessment(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent, bg = '#394552')

        self.parent = parent
        self.pack(side='left', fill='both', pady=26)
              
        nav_button=tk.Button(self, text='Assessments', width=25, anchor=tk.W, fg='white', font=("Calibri", 12, 'bold'), bg='#394552',
                          command=lambda: self.show_assessments())
        nav_button.grid(row=0, column=0, sticky=tk.W, pady=(10, 0), padx=10)
        
        nav_button.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
        nav_button=tk.Button(self, text='Create Assessments', width=25, bg='#394552', bd=0, fg='white', font=('Calibri', 12), anchor=tk.W,
                          command=lambda: self.create_assessment())
        nav_button.grid(row=2, column=0, sticky=tk.W, padx=30, pady=10)
        nav_button=tk.Button(self, text='Record Assessments', width=25, bg='#394552', fg='white', bd=0, font=('Calibri', 12), anchor=tk.W,
                          command=lambda: self.our_command)
        nav_button.grid(row=3, column=0, sticky=tk.W, padx=30, pady=10)        
        enroll_button=tk.Button(self, text='Evaluation', width=25, bg='#394552', bd=0, fg='white', font=('Calibri', 12), anchor=tk.W,
                          command=lambda: self.our_command)
        enroll_button.grid(row=4, column=0, sticky=tk.W, padx=30, pady=10)
        nav_button=tk.Button(self, text='Timetable', width=25, anchor=tk.W, fg='white', font=("Calibri", 12, 'bold'), bg='#394552', bd=0,
                          command=lambda: self.our_command)
        nav_button.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        nav_button=tk.Button(self, text='Notes', width=25, anchor=tk.W, fg='white', font=("Calibri", 12, 'bold'), bg='#394552', bd=0,
                          command=lambda: self.our_command)
        nav_button.grid(row=6, column=0, sticky=tk.W, padx=10)
        
    
    def show_assessments(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create class treeview frame
        self.parent.treeview = AssessmentTreeview(self.parent)

    def create_assessment(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create class treeview frame
        self.parent.assess_frame = CreateAssessment(self.parent)
        
    
    def enroll_class_in_course(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create add course treeview frame
        self.parent.treeview = ClassTreeviewII(self.parent)
        
    def add_student(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create student treeview frame
        self.parent.treeview = StudentTreeview(self.parent)
    
    def upload_student(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create student treeview frame
        self.parent.treeview = UploadStudentTreeview(self.parent)
    
    # Click command
    def our_command(self):
        pass 
        
    