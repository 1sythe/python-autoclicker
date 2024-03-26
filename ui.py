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

        self.geometry('500x400')
        self.resizable(False, False)
        self.title("AutoClicker")
        self.option_add("*tearOff", False)

        self.setup_visuals()
        self.setup_ui()

        self.clicker = Clicker(1, Controller())
        self.click_thread = threading.Thread(target=self.clicker.click, daemon=True)

    def setup_visuals(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        style = ttk.Style(self)
        self.tk.call("source", "assets/theme.tcl")
        style.theme_use("equilux")

        self.font_large = customtkinter.CTkFont(family='Comfortaa', size=25, weight='bold')
        self.font_medium = customtkinter.CTkFont(family='Comfortaa', size=20, weight='bold')
        self.font_small = customtkinter.CTkFont(family='Comfortaa', size=15)
        self.font_small_thick = customtkinter.CTkFont(family='Comfortaa', size=14, weight='bold')
        self.font_mini = customtkinter.CTkFont(family='Comfortaa', size=11)

    def setup_ui(self):
        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(pady=3, padx=3, fill="both", expand=True)

        customtkinter.CTkLabel(master=main_frame, text="AutoClicker", font=self.font_large).pack()


        # Mouse autoclicker frame, content
        mouse_frame = customtkinter.CTkFrame(master=main_frame)
        mouse_frame.place(relx=0, rely=0.12, relwidth=0.495, relheight=0.4)

        mouse_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        mouse_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')

        customtkinter.CTkLabel(master=mouse_frame, text="Mouse", font=self.font_medium).grid(column=1, row=0,
                                                                                             sticky="w", columnspan=3)

        # Clickspeedunitframe, content

        def change_mousespeed_unit(choice):
            if choice == "Intervall":
                mouse_intervall_frame.lift()

            else:
                mouse_cps_frame.lift()

        mouse_speed_unit_optionmenu = customtkinter.CTkOptionMenu(master=mouse_frame, values=["Cps", "Intervall"],
                                                              command=change_mousespeed_unit, width=100)
        mouse_speed_unit_optionmenu.grid(column=2, row=0, padx=5, pady=3, sticky="w", columnspan=2)


        # Cpsunit frame
        mouse_cps_frame = customtkinter.CTkFrame(master=mouse_frame)
        mouse_cps_frame.place(relx=0, rely=0.22, relwidth=1, relheight=0.45)

        customtkinter.CTkLabel(master=mouse_cps_frame, text="Clickspeed in Cps:", font=self.font_small_thick).pack(pady=2)

        self.mouse_cps_entry = customtkinter.CTkEntry(master=mouse_cps_frame, font=self.font_small, width=50)
        self.mouse_cps_entry.pack(pady=7)

        # Intervallunit frame
        mouse_intervall_frame = customtkinter.CTkFrame(master=mouse_frame)
        mouse_intervall_frame.place(relx=0, rely=0.22, relwidth=1, relheight=0.45)
        mouse_intervall_frame.lower()

        mouse_intervall_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        mouse_intervall_frame.rowconfigure((0, 1, 2), weight=1, uniform='a')

        customtkinter.CTkLabel(master=mouse_intervall_frame,
                               text="Clickspeed intervall:", font=self.font_small_thick).grid(column=0, row=0, columnspan=3)

        customtkinter.CTkLabel(master=mouse_intervall_frame, text="Minutes:", font=self.font_mini).grid(column=0, row=1)
        self.mouse_minute_entry = customtkinter.CTkEntry(master=mouse_intervall_frame, font=self.font_small, width=50,)
        self.mouse_minute_entry.grid(column=0, row=2, pady=2)

        customtkinter.CTkLabel(master=mouse_intervall_frame, text="Seconds:", font=self.font_mini).grid(column=1, row=1)
        self.mouse_sec_entry = customtkinter.CTkEntry(master=mouse_intervall_frame, font=self.font_mini, width=50)
        self.mouse_sec_entry.grid(column=1, row=2, pady=2)

        customtkinter.CTkLabel(master=mouse_intervall_frame, text="Milliseconds:", font=self.font_mini).grid(column=2, row=1)
        self.mouse_milsec_entry = customtkinter.CTkEntry(master=mouse_intervall_frame, font=self.font_mini, width=50)
        self.mouse_milsec_entry.grid(column=2, row=2, pady=2)



        # Mbutton selection

        customtkinter.CTkLabel(master=mouse_frame, text="Select Mousebutton:", font=self.font_small).grid(column=0, row=4,
                                                                            columnspan=2, rowspan=2, pady=10, padx=2)


        mbutton_select_optionmenu = customtkinter.CTkOptionMenu(master=mouse_frame,
                                                                values=["Left button", "Right button"], width=50, height=20)

        mbutton_select_optionmenu.grid(column=2, row=4, columnspan=2, rowspan=2, pady=10, sticky="w")



        # Key autoclicker frame, content
        key_frame = customtkinter.CTkFrame(master=main_frame)
        key_frame.place(relx=0.5, rely=0.12, relwidth=0.495, relheight=0.4)

        customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=self.font_medium).pack()


        # Operating(start/stop) frame, content
        operating_frame = customtkinter.CTkFrame(master=main_frame)
        operating_frame.place(relx=0, rely=0.53, relwidth=1, relheight=0.2)


        operating_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        operating_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        # Switch button
        autoclicker_switch = customtkinter.CTkSwitch(master=operating_frame, text="")
        autoclicker_switch.grid(column=1, row=0, sticky="e")

        customtkinter.CTkLabel(master=operating_frame, text="Mouse autoclicker", font=self.font_small).grid(column=0, row=0, columnspan=2)
        customtkinter.CTkLabel(master=operating_frame, text="Key autoclicker", font=self.font_small).grid(column=1, row=0, columnspan=2)


        start_button = customtkinter.CTkButton(master=operating_frame, text="Start", font=self.font_medium, command=self.start_clicker)
        start_button.grid(column=0, row=1, rowspan=2)

        stop_button = customtkinter.CTkButton(master=operating_frame, text="Stop", font=self.font_medium, command=self.stop_clicker)
        stop_button.grid(column=2, row=1, rowspan=2)



    def start_clicker(self):
        self.clicker.interval = float(self.mouse_interval_entry.get())
        self.click_thread.start()

    def stop_clicker(self):
        # TODO: add metrics
        self.clicker.running = False


if __name__ == "__main__":
    app = AutoClickerApp()
    app.mainloop()
    #threading.Thread(target=AutoClickerApp().mainloop).start()