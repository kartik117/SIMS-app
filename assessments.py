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
        
        # Add Buttons
        add_button = ttk.Button(self, text="Add Pic", command=lambda: self.add_profile_picture(), width=42)
        add_button.grid(row=2, column=4, padx=10, pady=5, columnspan=2)
        
        
        
        
        
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
                self.img = ImageTk.PhotoImage(self.img, master=self)
                
            except(ValueError):
                messagebox.showerror("File Error", "File could not be opened... try again!")
            except FileNotFoundError:
                messagebox.showerror("File Error", "File could not be found... try again!")
                
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1260, height=550)
        self.my_canvas.grid(row=0, column = 0)
        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')        

