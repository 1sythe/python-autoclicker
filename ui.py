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


#visuals
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    style = ttk.Style(root)
    root.tk.call("source", "assets/theme.tcl")
    style.theme_use("equilux")

#fonts
    font_large = customtkinter.CTkFont(family='Comfortaa', size=25, weight='bold')
    font_medium = customtkinter.CTkFont(family='Comfortaa', size=20, weight='bold')
    font_small = customtkinter.CTkFont(family='Comfortaa', size=15)
    font_mini = customtkinter.CTkFont(family='Comfortaa', size=10)


#main frame
    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(pady=3, padx=3, fill="both", expand=True)

    customtkinter.CTkLabel(master=main_frame, text="Autoclicker", font=font_large).pack()




#mouse autoclicker frame
    mouse_frame = customtkinter.CTkFrame(master=main_frame)
    mouse_frame.place(relx=0, rely=0.12, relwidth=0.5, relheight=0.4)

    mouse_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
    mouse_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

    customtkinter.CTkLabel(master=mouse_frame, text="Mouse", font=font_medium).grid(column=1, row=0, sticky="nswe")
    customtkinter.CTkLabel(master=mouse_frame, text="Speed", font=font_small).grid(column=0, row=1, sticky="w", columnspan=2)

    mouse_intervall_entry = customtkinter.CTkEntry(master=mouse_frame, font=font_mini, placeholder_text="Intervall")
    mouse_intervall_entry.grid(column=0, row=2, padx=5)

    mouse_cps_entry = customtkinter.CTkEntry(master=mouse_frame, font=font_mini, placeholder_text="Cps")
    mouse_cps_entry.grid(column=2, row=2, padx=5)

    customtkinter.CTkLabel(master=mouse_frame, text="sec", font=font_small).grid(column=1, row=2, sticky='w')




    #key autoclicker frame
    key_frame = customtkinter.CTkFrame(master=main_frame)
    key_frame.place(relx=0.5, rely=0.12, relwidth=0.5, relheight=0.4)

    customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=font_medium).pack()


#frame for start/stop etc.
    operating_frame = customtkinter.CTkFrame(master=main_frame)
    operating_frame.place(relx=0, rely=0.53, relwidth=1, relheight=0.2)

    operating_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
    operating_frame.rowconfigure((0, 1), weight=1, uniform='a')

    start_button = customtkinter.CTkButton(master=operating_frame, text="start", font=font_medium)
    start_button.pack(padx=5, side="left")

    stop_button = customtkinter.CTkButton(master=operating_frame, text="stop", font=font_medium)
    stop_button.pack(padx=5, side="right")


    root.mainloop()


startup()