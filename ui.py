import tkinter as tk
import tkinter.font as font
import customtkinter
import threading

from tkinter import *
from tkinter import ttk
from clicker import Clicker
from pynput.mouse import Controller, Button


class AutoClickerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('400x300')
        self.resizable(False, False)
        self.title("AutoClicker")
        self.option_add("*tearOff", False)

        self.setup_visuals()
        self.setup_ui()

    def setup_visuals(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        style = ttk.Style(self)
        self.tk.call("source", "assets/theme.tcl")
        style.theme_use("equilux")

        self.font_large = customtkinter.CTkFont(family='Comfortaa', size=25, weight='bold')
        self.font_medium = customtkinter.CTkFont(family='Comfortaa', size=20, weight='bold')
        self.font_small = customtkinter.CTkFont(family='Comfortaa', size=15)
        self.font_mini = customtkinter.CTkFont(family='Comfortaa', size=11)

    def setup_ui(self):
        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(pady=3, padx=3, fill="both", expand=True)

        customtkinter.CTkLabel(master=main_frame, text="AutoClicker", font=self.font_large).pack()


        # Mouse autoclicker frame, content
        mouse_frame = customtkinter.CTkFrame(master=main_frame)
        mouse_frame.place(relx=0, rely=0.12, relwidth=0.5, relheight=0.4)

        mouse_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        mouse_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        customtkinter.CTkLabel(master=mouse_frame, text="Mouse", font=self.font_medium).grid(column=1, row=0, sticky="nswe")
        customtkinter.CTkLabel(master=mouse_frame, text="Speed", font=self.font_small).grid(column=0, row=1,  padx=5, sticky="w", columnspan=2)

        self.mouse_interval_entry = customtkinter.CTkEntry(master=mouse_frame, font=self.font_mini, placeholder_text="Interval")
        self.mouse_interval_entry.grid(column=0, row=2, padx=5)

        mouse_cps_entry = customtkinter.CTkEntry(master=mouse_frame, font=self.font_mini, placeholder_text="Cps")
        mouse_cps_entry.grid(column=2, row=2, padx=5)

        customtkinter.CTkLabel(master=mouse_frame, text="sec", font=self.font_small).grid(column=1, row=2, sticky='w')

        # Mbutton selection
        mb_selection_var = IntVar()

        mouse_select_leftbutton = customtkinter.CTkRadioButton(master=mouse_frame, text="Left button",
                                                               font=self.font_mini, value=1, variable=mb_selection_var,
                                                               radiobutton_height=10, radiobutton_width=10)
        mouse_select_rightbutton = customtkinter.CTkRadioButton(master=mouse_frame, text="Right button",
                                                               font=self.font_mini, value=2, variable=mb_selection_var,
                                                               radiobutton_height=10, radiobutton_width=10)

        mouse_select_leftbutton.grid(column=0, row=3, columnspan=2, rowspan=2, pady=10)
        mouse_select_rightbutton.grid(column=1, row=3, columnspan=2, rowspan=2, pady=10, padx=25)



        # Key autoclicker frame, content
        key_frame = customtkinter.CTkFrame(master=main_frame)
        key_frame.place(relx=0.5, rely=0.12, relwidth=0.5, relheight=0.4)

        customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=self.font_medium).pack()


        # Operating(start/stop) frame, content
        operating_frame = customtkinter.CTkFrame(master=main_frame)
        operating_frame.place(relx=0, rely=0.53, relwidth=1, relheight=0.2)


        operating_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        operating_frame.rowconfigure((0, 1), weight=1, uniform='a')

        start_button = customtkinter.CTkButton(master=operating_frame, text="Start", font=self.font_medium, command=self.start_clicker)
        start_button.pack(padx=5, side="left")

        stop_button = customtkinter.CTkButton(master=operating_frame, text="Stop", font=self.font_medium, command=self.stop_clicker)
        stop_button.pack(padx=5, side="right")

    def start_clicker(self):
        interval = float(self.mouse_interval_entry.get())

    def stop_clicker(self):
        pass


if __name__ == "__main__":
    clicker = Clicker(0.25, Controller())

    app = AutoClickerApp()
    app.mainloop()
    #threading.Thread(target=AutoClickerApp().mainloop).start()