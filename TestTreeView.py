# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 12:55:00 2022

@author: KAIZEN
"""
import tkinter as tk
from tkinter import ttk


class TestTreeView(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from dashboard import Dashboard

        self.tree = CourseTreeview(self, parent)
          
    def menubar(self, root):
        menubar = tk.Menu(root)
        return(menubar)