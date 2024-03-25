import tkinter as tk
import tkinter.font as font

from tkinter import ttk
from clicker import Clicker
from pynput.mouse import Controller, Button


def startup():
    root = tk.Tk()

    root.geometry('450x400')
    root.resizable(False, False)
    root.title("Autlicker by Sythe (& rowbow)")
    root.option_add("*tearOff", False)

    style = ttk.Style(root)
    root.tk.call("source", "assets/theme.tcl")
    style.theme_use("equilux")

    font_large = font.Font(family='Comfortaa', size='28', weight='bold')
    font_medium = font.Font(family='Comfortaa', size='20', weight='bold')
    font_small = font.Font(family='Comfortaa', size='15')

    clicker = Clicker(0.25, Controller())
    tk.Button(root, text="start", font=font_medium, command=clicker.start).pack()
    tk.Button(root, text="stop", font=font_medium, command=clicker.stop).pack()

    root.mainloop()


if __name__ == "__main__":
    startup()
