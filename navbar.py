# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:55:41 2022

@author: KAIZEN
"""


import tkinter as tk
from tkinter import ttk



from classtreeview import ClassTreeview
from classtreeviewupdate import ClassTreeviewII
from coursetreeview import CourseTreeview
from student_treeview import StudentTreeview
from student_treeview_upload import UploadStudentTreeview

from db_srms_sqlite import Database
db = Database('new_single_user3.db')

class NavBar(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent, bg = '#f3f3f4')

        self.parent = parent
        self.pack(side='left', fill='both', pady=18)
              
        nav_button=tk.Button(self, text='My Courses', width=25, anchor=tk.W, font=("Calibri", 10, 'bold italic'), bg='#f3f3f4',
                          command=lambda: self.show_courses())
        nav_button.grid(row=0, column=0, sticky=tk.W, pady=(10, 0), padx=10)
        nav_button=tk.Button(self, text='My Classes', width=25, anchor=tk.W, font=("Calibri", 10, 'bold italic'), bg='#f3f3f4', bd=0,
                          command=lambda: self.show_classes())
        nav_button.grid(row=1, column=0, sticky=tk.W, pady=10, padx=10)
        nav_button=tk.Button(self, text='Add/Edit Students', width=25, bg='#f3f3f4', bd=0, anchor=tk.W,
                          command=lambda: self.add_student())
        nav_button.grid(row=2, column=0, sticky=tk.W, padx=30, pady=10)
        nav_button=tk.Button(self, text='Upload Students List', width=25, bg='#f3f3f4', bd=0, anchor=tk.W,
                          command=lambda: self.upload_student())
        nav_button.grid(row=3, column=0, sticky=tk.W, padx=30, pady=10)        
        enroll_button=tk.Button(self, text='Enroll Class', width=25, bg='#f3f3f4', bd=0, anchor=tk.W,
                          command=lambda: self.enroll_class_in_course())
        enroll_button.grid(row=4, column=0, sticky=tk.W, padx=30, pady=10)
        nav_button=tk.Button(self, text='Timetable', width=25, anchor=tk.W, font=("Calibri", 10, 'bold italic'), bg='#f3f3f4', bd=0,
                          command=lambda: self.our_command)
        nav_button.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        nav_button=tk.Button(self, text='Notes', width=25, anchor=tk.W, font=("Calibri", 10, 'bold italic'), bg='#f3f3f4', bd=0,
                          command=lambda: self.our_command)
        nav_button.grid(row=6, column=0, sticky=tk.W, padx=10)
        
    
    def show_courses(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create class treeview frame
        self.parent.treeview = CourseTreeview(self.parent)

    def show_classes(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create class treeview frame
        self.parent.treeview = ClassTreeview(self.parent)
    
    def enroll_class_in_course(self):
        # Clear off whichever frame is currently displayed
        self.parent.winfo_children()[1].destroy()
        # Create add course treeview frame
        self.parent.treeview = ClassTreeviewII(self.parent)
                
                # NOTES:
                # Might have to build another frame that contains in addition to the remaining widgets, a combobox widget for adding courses
                # self.parent.winfo_children()[1].destroy()
                # self.parent.treeview = ClassTreeviewWITHcombobox(self.parent)
                # Or (and this would be fun) create the replacement widget here: hahahahahaha!!! I thought it would not be possible but it just might work
        
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
        
    