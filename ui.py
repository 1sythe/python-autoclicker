import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import customtkinter


def startup():

    root = customtkinter.CTk()

    root.geometry('400x300')
    root.resizable(False, False)
    root.title("Autoclicker")
    root.option_add("*tearOff", False)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    style = ttk.Style(root)
    root.tk.call("source", "assets/theme.tcl")
    style.theme_use("equilux")

    font_large = font.Font(family='Comfortaa', size='28', weight='bold')
    font_medium = font.Font(family='Comfortaa', size='20', weight='bold')
    font_small = font.Font(family='Comfortaa', size='15')






    root.mainloop()


startup()