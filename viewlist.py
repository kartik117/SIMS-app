# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:55:00 2022

@author: KAIZEN
"""
import tkinter as tk
from tkinter import ttk

from db_srms_sqlite import Database1
db1 = Database1('new_single_user3.db')


class ViewList(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Placed here to avoid Import error clash with Dashboard 'circular imports'
        from dashboard import Dashboard
        courses = db1.fetch_course()
        for course in courses:
            # Label frame
            # Spacing is to avoid multiple labelling
            self.frame = tk.LabelFrame(self, text = " Course                                                                          Students ")
            self.frame.pack(padx=10, pady=10)
            # Students List (Listbox)
            self.students_list = tk.Listbox(self.frame, height=12, width=78)
            self.students_list.grid(row=3 + 6*(int(courses.index(course))), column=2, columnspan=2, rowspan=6, padx=(5, 5))

            # Create scrollbar
            scrollbar= tk.Scrollbar(self.frame)
            scrollbar.grid(row=3 + 6*(int(courses.index(course))), column=4,rowspan=6, sticky=(tk.N, tk.S, tk.W))

            # Set scroll to listbox
            self.students_list.configure(yscrollcommand=scrollbar.set)
            scrollbar.configure(command=self.students_list.yview)
 
            # Course_entry
            self.course_text = tk.StringVar()
            self.course_entry = tk.Entry(self.frame, textvariable=self.course_text, width=40)
            self.course_entry.grid(row=3 + 6*(int(courses.index(course))), column=1, padx=5, sticky=tk.W)
            self.course_entry.insert(tk.END, course[0])
            
            
            self.class_text = tk.StringVar()
            self.class_entry = tk.Entry(self.frame, textvariable=self.class_text, width=40)
            self.class_entry.grid(row=5 + 6*(int(courses.index(course))), column=1, padx=5, sticky=tk.W)
            #self.class_entry.insert(tk.END, student_class)
            
            # Stringify the output from the database from {course} to 'course'
            #new_course = course[0]
            #self.populate_view_list(new_course)
            
            home_button=tk.Button(self.frame, text='Back to Home', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=0, column=6, pady=(10, 0))
            home_button=tk.Button(self.frame, text='Select videos', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=1, column=6)
            home_button=tk.Button(self.frame, text='Test Menu', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=2, column=6)
            home_button=tk.Button(self.frame, text='Projets', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=3, column=6)
            home_button=tk.Button(self.frame, text='Console', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=4, column=6)
            home_button=tk.Button(self.frame, text='Help', width=15, bd=0,
                              command=lambda: controller.show_frame(Dashboard))
            home_button.grid(row=5, column=6)

    
    '''  
    def populate_view_list(self, course_name_here):
        self.students_list.delete(0, tk.END)
        for row in db1.fetch_students_in_course(course_name_here):
            self.students_list.insert(tk.END, row)
    '''         
    
    def menubar(self, root):
        menubar = tk.Menu(root)
        return(menubar)