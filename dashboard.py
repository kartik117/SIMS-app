# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:48:43 2022

@author: KAIZEN
"""

import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog

from navbar import NavBar
from coursetreeview import CourseTreeview

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#f3f3f4')
             
        self.controller = controller
        self.nav = NavBar(self, parent)
        self.tree = CourseTreeview(self)
        
    def get_name(self):
        # check if login username entry matches username and if login password entry matches password
        with open("single user", "r") as file:
            file_data = file.read()
        
        file_data = file_data.split('\n')
        self.name = file_data[0].title()      
        return self.name
    
    def menubar(self, controller):
        menubar = tk.Menu(controller)
        
        # Create a menu item (Set tearoff  to false to disable detachable submenu)
        fileMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Open", command=lambda: self.file_open())
        fileMenu.add_separator()
        fileMenu.add_command(label="Open last closed", command=self.our_command)
        fileMenu.add_command(label="Open folder", command=self.our_command)
        
        # Create Edit menu
        editMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Edit", menu=editMenu)
        # Edit menu items
        editMenu.add_command(label="Cut", command=self.our_command)
        editMenu.add_command(label="Copy", command=self.our_command)
        
        # Create Options menu
        optionsMenu= tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Options", menu=optionsMenu)
        # Options menu items
        optionsMenu.add_command(label="Add new course", command=lambda: self.add_new_course())
        optionsMenu.add_command(label="Add lecture notes", command=self.our_command)
        optionsMenu.add_command(label="View list", command=self.our_command)

        
        # Create Records menu
        recordsMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Records", menu=recordsMenu)
        # records menu items
        recordsMenu.add_command(label="New/Edit", command=self.our_command)
        recordsMenu.add_command(label="Load existing", command=self.our_command)     

        # To be deleted soon
        #recordsMenu.add_command(label="Student Reports", command=lambda: root.show_frame(StudentDetails))
        #recordsMenu.add_command(label="Class Reports", command=lambda: root.show_frame(ClassDetails))
                
        # Create Analytics menu
        analyticsMenu= tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Analytics", menu=analyticsMenu)
        # Options analytics items
        analyticsMenu.add_command(label="Student", command=self.our_command)
        analyticsMenu.add_command(label="Class", command=self.our_command)
        analyticsMenu.add_command(label="Course", command=self.our_command)
        
        # Create Attendance menu
        attendanceMenu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Attendance", menu=attendanceMenu)
        # Attendance menu items
        attendanceMenu.add_command(label="New", command=self.our_command)
        attendanceMenu.add_command(label="View log", command=self.our_command)
        attendanceMenu.add_command(label="Add existing log", command=self.our_command)
       
        # Create Help menu
                # tk.docs says something about help menu. Check it out.
        helpMenu= tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Help", menu=helpMenu)
        # Options help items
        helpMenu.add_command(label="About SRMS", command=self.our_command)
        helpMenu.add_command(label="FAQ", command=self.our_command)
        helpMenu.add_command(label="SRMS documentation", command=self.our_command)
        helpMenu.add_command(label="Tutorial", command=self.our_command)
        helpMenu.add_command(label="Check for updates", command=self.our_command)
        helpMenu.add_command(label="Troubeshooting", command=self.our_command)
        
        return(menubar)
    
    # Create file open function
    def file_open(self):
        filename = filedialog.askopenfilename(
            initialdir = "C:/Documents",
            title = "Open A File",
            filetype = (("xlsx files", "*.xlsx"), ("All Files", "*.*"))
            )
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
                
            except(ValueError):
                pass#my_label.config(text="File couldn't be opened... try again!")
                
            except FileNotFoundError:
                pass#my_label.config(text="File could not be found... try again!")   
    
    # Click command
    def our_command(self):
        pass 
    
           
    
  