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

    font_large = customtkinter.CTkFont(family='Comfortaa', size=25, weight='bold')
    font_medium = customtkinter.CTkFont(family='Comfortaa', size=20, weight='bold')
    font_small = customtkinter.CTkFont(family='Comfortaa', size=15)

    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(pady=3, padx=3, fill="both", expand=True)

    customtkinter.CTkLabel(master=main_frame, text="Autoclicker", font=font_large).pack()


    mouse_frame = customtkinter.CTkFrame(master=main_frame)
    mouse_frame.place(relx=0, rely=0.12, relwidth=0.5, relheight=0.4)

    mouse_frame.columnconfigure((0,1,2), weight=1, uniform='a')
    mouse_frame.rowconfigure((0,1,2,3,4), weight=1, uniform='a')


    key_frame = customtkinter.CTkFrame(master=main_frame)
    key_frame.place(relx=0.5, rely=0.12, relwidth=0.5, relheight=0.4)

    customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=font_medium).pack()



    operating_frame = customtkinter.CTkFrame(master=main_frame)
    operating_frame.place(relx=0, rely=0.53, relwidth=1, relheight=0.25)






    root.mainloop()


startup()