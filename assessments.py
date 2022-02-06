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

from db_srms_sqlite import Database
db = Database('new_single_user3.db')


class CreateAssessment(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='left', fill='both', expand=True)
        
        sess_assess_frame = tk.Frame(self) # wraps around session and assessment frames to keep them aligned
        sess_assess_frame.pack(side='left', fill='both', pady=26, padx=15)
        
        session_frame = tk.LabelFrame(sess_assess_frame, bg='white', borderwidth=0)
        session_frame.pack(side='top', fill='x', anchor=tk.N)
        
        # Create session dropdown menu
        session_label = tk.Label(session_frame, text="Academic Year", bg='white')
        session_label.grid(row=0,column=0, pady=(10, 20), padx=10, sticky='W')
        self.session_select = tk.StringVar()
        session_dropdown_list = ["Select session"] 
         # Get list of sessions from database
        #db_fetch_session_list = [session[1] for session in db.fetch_session()]
         # Concatenate both lists 
        #session_dropdown_list += db_fetch_session_list
        session_dropdown_menu = ttk.OptionMenu(session_frame, self.session_select, *session_dropdown_list)
        session_dropdown_menu.grid(row=1, column=0, pady=(0,30), padx=10)
        
        # Create term dropdown menu
        term_label=tk.Label(session_frame, text="Term", bg='white')
        term_label.grid(row=2, column=0, pady=(20, 10), padx=10, sticky='W')
        self.term_select = tk.StringVar()
        self.term_dropdown_list = ["Select term", "1", "2", "3"]
        term_dropdown_menu = ttk.OptionMenu(session_frame, self.term_select, *self.term_dropdown_list)
        term_dropdown_menu.grid(row=3, column=0, pady=(5,80), padx=10)
        
        # Create course frame
        course_frame = tk.LabelFrame(sess_assess_frame, bg='white', borderwidth=0)
        course_frame.pack(side='bottom', fill='both', expand=True, pady=(15,0))
        # Create course dropdown menu as attribute of course frame.
        course_label = tk.Label(course_frame, text="Course", bg='white')
        course_label.grid(row=0,column=0, padx=10, sticky='W')
        
        self.course_select = tk.StringVar()
        self.course_dropdown_list = ["Select course"]
        # Get list of courses from database
        db_fetch_course_list = [course[1] + "  " + course[2] for course in db.fetch_course()]
        # Concatenate both lists
        self.course_dropdown_list += db_fetch_course_list
        # Create dropdown menu of courses
        course_dropdown_menu = ttk.OptionMenu(course_frame, self.course_select, *self.course_dropdown_list)
        course_dropdown_menu.grid(row=1, column=0, pady=(5,30), padx=10)
                
        # Create class dropdown menu as attribute of course frame.
        class_label=tk.Label(course_frame, text="Class", bg='white')
        class_label.grid(row=2, column=0, pady=(100,0), padx=10, sticky='W')
        # Initiate class_list variable
        self.class_select = tk.StringVar()
        self.class_list = ['Select Class']
        # Get list of classes from database
        db_fetch_class_list = [class_pick[1] for class_pick in db.fetch_class()]
        # Concatenate both lists
        self.class_list += db_fetch_class_list
        # Create dropdown menu of classes
        class_dropdown_menu = ttk.OptionMenu(course_frame, self.class_select, *self.class_list)
        class_dropdown_menu.grid(row=3, column=0, pady=(5,80), padx=10)
        
        holder_frame = tk.Frame(self) # wraps around assessment frame
        holder_frame.pack(side='left', fill='both', pady=26)
        
        # Create assessment frame
        assessment_frame = tk.LabelFrame(holder_frame, bg='white', borderwidth=0, width=150)
        assessment_frame.pack(side='top',fill='both', expand=True)
        # Create assessment type dropdown menu
        assessment_label = tk.Label(assessment_frame, text="Assessment type", bg='white')
        assessment_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=10, sticky='W')
        # Set assessment variables and create checkboxes
        self.first_assessment_select = tk.StringVar()
        checkbox1 = ttk.Checkbutton(assessment_frame, text="First test", variable=self.first_assessment_select, onvalue="First test", offvalue="")
        checkbox1.grid(row=1, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.second_assessment_select = tk.StringVar()
        checkbox2 = ttk.Checkbutton(assessment_frame, text="Second test", variable=self.second_assessment_select, onvalue="Second test", offvalue="")
        checkbox2.grid(row=2, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.third_assessment_select = tk.StringVar()
        checkbox3 = ttk.Checkbutton(assessment_frame, text="Third test", variable=self.third_assessment_select, onvalue="Third test", offvalue="")
        checkbox3.grid(row=3, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.project_select = tk.StringVar()
        checkbox4 = ttk.Checkbutton(assessment_frame, text="Project", variable=self.project_select, onvalue="Project", offvalue="")
        checkbox4.grid(row=4, column=0, pady=(5,10), padx=10, sticky=tk.W)      
        self.assignment_select = tk.StringVar()
        checkbox5 = ttk.Checkbutton(assessment_frame, text="Assignment", variable=self.assignment_select, onvalue="Assignment", offvalue="")
        checkbox5.grid(row=5, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.home_work_select = tk.StringVar()
        checkbox6 = ttk.Checkbutton(assessment_frame, text="Home work", variable=self.home_work_select, onvalue="Home work", offvalue="")
        checkbox6.grid(row=6, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.lab_select = tk.StringVar()
        checkbox7 = ttk.Checkbutton(assessment_frame, text="Laboratory", variable=self.lab_select, onvalue="Laboratry", offvalue="")
        checkbox7.grid(row=7, column=0, pady=(5,10), padx=10, sticky=tk.W)
        self.examination_select = tk.StringVar()
        checkbox8 = ttk.Checkbutton(assessment_frame, text="Examination", variable=self.examination_select, onvalue="Examination", offvalue="")
        checkbox8.grid(row=8, column=0, pady=(5,10), padx=10, sticky=tk.W)
        # Set other_assessment variable and combobox
        self.other_assessment_select = tk.StringVar()
        self.other_assessment_list = ["Select other assessment"]
        other_assessments = ttk.Combobox(assessment_frame, values=self.other_assessment_list, width=25)
        other_assessments.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W)
        other_assessments.set(self.other_assessment_list[0])
        
        # Create maximum score entry boxes
        score= tk.Label(assessment_frame, text="Maximum score", bg='white')
        score.grid(row=0, column=3, pady=(10, 20), padx=10, sticky='W')
        score_box = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box.grid(row=1, column=3, pady=(0,10), padx=20)
        score_box1 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box1.grid(row=2, column=3, pady=9, padx=20)
        score_box2 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box2.grid(row=3, column=3, pady=9, padx=20)
        score_box3 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box3.grid(row=4, column=3, pady=9, padx=20)
        score_box4 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box4.grid(row=5, column=3, pady=9, padx=20)
        score_box5 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box5.grid(row=6, column=3, pady=9, padx=20)
        score_box6 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box6.grid(row=7, column=3, pady=9, padx=20)
        score_box7 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box7.grid(row=8, column=3, pady=9, padx=20)
        score_box8 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box8.grid(row=9, column=3, pady=9, padx=20)
       

class AssessmentTreeview(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='top', fill='both', expand=True)

        # Add Search Box (Rememeber to implement 'Search' showing in bar )
        search_box = tk.Entry(self, width=60)
        search_box.pack(pady=4, padx=2, anchor=tk.NE)

        # Add some style
        style = ttk.Style()
        # Pick a theme
        #style.theme_use("default")
        # Configure our treeview colours
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=20,
                        fieldbackground="#D3D3D3"
                        )
        # Change selected colour
        style.map('Treeview',
                  background=[('selected', '#73c2fb')]) #a4bce9

        # Create Treeview Frame
        tree_frame = tk.Frame(self)
        tree_frame.pack(fill=tk.X, anchor=tk.N, padx=(20, 0))

        # Treeview Scrollbar
        tree_scroll = tk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y, pady=(2,0))

        # Create Treeview
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended', height=25)
        # Pack to the screen
        self.my_tree.pack(fill=tk.X)

        # Configure scrollbar
        tree_scroll.config(command=self.my_tree.yview)

        # Define our columns. Reserve two extra null columns for subsequent child rows i.e student first and last names
        self.my_tree['columns'] = ('ID', 'R.Id', 'First name', 'Middle name', 'Last name', 'Class', 'Course', 'Assessment', 'Score')

        # Format our columns
        self.my_tree.column("#0", stretch=tk.NO, width=0)
        self.my_tree.column("ID", anchor=tk.CENTER, stretch=tk.NO, width=0)
        self.my_tree.column("R.Id", anchor=tk.W, stretch=tk.NO, width=30)
        self.my_tree.column("First name", anchor=tk.W, width=100)
        self.my_tree.column("Middle name", anchor=tk.W, width=100)
        self.my_tree.column("Last name", anchor=tk.W, width=100)
        self.my_tree.column("Class", anchor=tk.W, width=50)
        self.my_tree.column("Course", anchor=tk.W, width=200)
        self.my_tree.column("Assessment", anchor=tk.W, width=200)
        self.my_tree.column("Score", anchor=tk.W, width=1200)



        # Create Column headings
        self.my_tree.heading("#0", text="", anchor=tk.W)
        self.my_tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.my_tree.heading("R.Id", text="R.Id", anchor=tk.W)
        self.my_tree.heading("First name", text="First name", anchor=tk.W)
        self.my_tree.heading("Middle name", text="Middle name", anchor=tk.W)
        self.my_tree.heading("Last name", text="Last name", anchor=tk.W)
        self.my_tree.heading("Class", text="Class", anchor=tk.W)
        self.my_tree.heading("Course", text="Course", anchor=tk.W)
        self.my_tree.heading("Assessment", text="Assessment", anchor=tk.W)
        self.my_tree.heading("Score", text="Score", anchor=tk.W)


        # Create striped Treeview rows
        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#f3f3f4")
        
        
class AssessmentCombined(tk.Frame):
    def __init__(self, parent): 
        tk.Frame.__init__(self, parent)
        
        self.pack(side='left', fill='both', expand=True)
        
        holder_frame = tk.Frame(self) # wraps around session and assessment frames to keep them aligned
        holder_frame.pack(side='left', fill='both', pady=26, padx=(17,0))
        
        course_frame = tk.LabelFrame(holder_frame, bg='white', borderwidth=0)
        course_frame.pack(side='top', fill='x', anchor=tk.N)
        
        # Create course dropdown menu as attribute of course frame.
        course_label = tk.Label(course_frame, text="Course", bg='white')
        course_label.grid(row=0,column=0, padx=10, sticky='W')
        
        self.course_select = tk.StringVar()
        self.course_dropdown_list = ["Select course"]
        # Get list of courses from database
        db_fetch_course_list = [course[1] + "  " + course[2] for course in db.fetch_course()]
        # Concatenate both lists
        self.course_dropdown_list += db_fetch_course_list
        # Create dropdown menu of courses
        course_dropdown_menu = ttk.OptionMenu(course_frame, self.course_select, *self.course_dropdown_list)
        course_dropdown_menu.grid(row=1, column=0, pady=(5,30), padx=10)
                
        # Create class dropdown menu as attribute of course frame.
        class_label=tk.Label(course_frame, text="Class", bg='white')
        class_label.grid(row=2, column=0, pady=(20,0), padx=10, sticky='W')
        # Initiate class_list variable
        self.class_select = tk.StringVar()
        self.class_list = ['Select Class']
        # Get list of classes from database
        db_fetch_class_list = [class_pick[1] for class_pick in db.fetch_class()]
        # Concatenate both lists
        self.class_list += db_fetch_class_list
        # Create dropdown menu of classes
        class_dropdown_menu = ttk.OptionMenu(course_frame, self.class_select, *self.class_list)
        class_dropdown_menu.grid(row=3, column=0, pady=(5,80), padx=10)
        
        # Create assessment frame
        assessment_frame = tk.LabelFrame(holder_frame, bg='white', borderwidth=0)
        assessment_frame.pack(side='bottom',fill='both', expand=True, pady=(15,0))
        # Create assessment type dropdown menu
        assessment_label = tk.Label(assessment_frame, text="Assessment type", bg='white')
        assessment_label.grid(row=3, column=0, columnspan=2, pady=(40, 20), padx=10, sticky='W')
        self.assessment_select = tk.StringVar()
        self.assessment_list = ["Select assessment"]
        assessment_dropdown_menu = ttk.OptionMenu(assessment_frame, self.assessment_select, *self.assessment_list)
        assessment_dropdown_menu.grid(row=4, column=0, columnspan=2, pady=(5,10), padx=10)
        
        self.assessment_select1 = tk.StringVar()
        self.assessment_list1 = ["Select assessment"]
        assessment_dropdown_menu1 = ttk.OptionMenu(assessment_frame, self.assessment_select1, *self.assessment_list1)
        assessment_dropdown_menu1.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
        
        self.assessment_select2 = tk.StringVar()
        self.assessment_list2 = ["Select assessment"]
        assessment_dropdown_menu2 = ttk.OptionMenu(assessment_frame, self.assessment_select2, *self.assessment_list2)
        assessment_dropdown_menu2.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        
        self.assessment_select3 = tk.StringVar()
        self.assessment_list3 = ["Select assessment"]
        assessment_dropdown_menu3 = ttk.OptionMenu(assessment_frame, self.assessment_select3, *self.assessment_list3)
        assessment_dropdown_menu3.grid(row=7, column=0, columnspan=2, pady=10, padx=10)
        
        self.assessment_select4 = tk.StringVar()
        self.assessment_list4 = ["Select assessment"]
        assessment_dropdown_menu4 = ttk.OptionMenu(assessment_frame, self.assessment_select4, *self.assessment_list4)
        assessment_dropdown_menu4.grid(row=8, column=0, columnspan=2, pady=10, padx=10)
        
        score= tk.Label(assessment_frame, text="Score", bg='white')
        score.grid(row=3, column=3, padx=20, pady=(40, 20))
        score_box = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box.grid(row=4, column=3, pady=(0,10), padx=20)
        score_box1 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box1.grid(row=5, column=3, pady=10, padx=20)
        score_box2 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box2.grid(row=6, column=3, pady=10, padx=20)
        score_box3 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box3.grid(row=7, column=3, pady=10, padx=20)
        score_box4 = tk.Entry(assessment_frame, text=score, width=15, borderwidth=0, bg='#f3f3f4')
        score_box4.grid(row=8, column=3, pady=10, padx=20)
        
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
            