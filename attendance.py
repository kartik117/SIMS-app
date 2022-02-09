# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:02:24 2022

@author: KAIZEN
"""

import tkinter as tk
from tkinter import ttk
from db_sims_sqlite import Database

db = Database('new_single_user3.db')

class Attendance(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack(side='top', fill='both', expand=True)
        
        # Create View Frame
        self.view_frame = tk.Frame(self)
        self.view_frame.pack(side='top', fill='both', expand=True, )
        
        #view_frame = tk.Frame(self)
        #view_frame.pack(side='top', fill='both', expand=True )

        
        # View Scrollbar
        self.view_scroll = tk.Scrollbar(self.view_frame, orient="vertical")
        self.view_scroll.pack(side=tk.RIGHT, fill=tk.Y, pady=(2,0), command=self.view_frame.yview)
        
        self.view_frame['yscrollcommand'] = self.view_scroll.set
        # Course attendance
        students_list = [student for student in db.fetch_students_in_class('SS3')]

        for i in range(0, 100):
            student_frame = tk.LabelFrame(self.view_frame, bg='white', borderwidth=0)
            student_frame.pack(pady=5, padx=5)
            button = tk.Button(student_frame, text=i)
            button.grid(row=0, column=1)
            
        # Configure scrollbar
        #self.view_scroll.config(command=self.view_frame.yview)

# Test
def main():
    students_list = [student for student in db.fetch_students_in_class('SS3')]



    for student in students_list:
        print(students_list.index(student))


if __name__ == '__main__':
    main()