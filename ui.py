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


    def on_focus_in(entry):
        if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')

    def on_focus_out(entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled')


    mouse_frame = customtkinter.CTkFrame(master=main_frame)
    mouse_frame.place(relx=0, rely=0.12, relwidth=0.5, relheight=0.4)

    mouse_frame.columnconfigure((0,1,2), weight=1, uniform='a')
    mouse_frame.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

    customtkinter.CTkLabel(master=mouse_frame, text="Mouse", font=font_medium).grid(column=1, row=0, sticky="nswe")
    customtkinter.CTkLabel(master=mouse_frame, text="Speed", font=font_small).grid(column=0, row=1, sticky="w", columnspan=2)

    mouse_intervall_entry = customtkinter.CTkEntry(master=mouse_frame, font=font_small)
    mouse_intervall_entry.grid(column=0, row=2)
    mouse_intervall_entry.insert(0, "intervall in ms")
    mouse_intervall_entry.configure(state='disabled')

    mouse_cps_entry = customtkinter.CTkEntry(master=mouse_frame, font=font_small)
    mouse_cps_entry.grid(column=2, row=2)
    mouse_cps_entry.insert(0, "speed in cps")
    mouse_cps_entry.configure(state='disabled')

    key_frame = customtkinter.CTkFrame(master=main_frame)
    key_frame.place(relx=0.5, rely=0.12, relwidth=0.5, relheight=0.4)

    customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=font_medium).pack()



    operating_frame = customtkinter.CTkFrame(master=main_frame)
    operating_frame.place(relx=0, rely=0.53, relwidth=1, relheight=0.25)





    root.mainloop()


startup()