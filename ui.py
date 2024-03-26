import tkinter
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

        self.geometry('300x400')
        self.resizable(False, False)
        self.title("AutoClicker")
        self.option_add("*tearOff", False)

        self.setup_visuals()
        self.setup_ui()

        self.clicker = Clicker(1, Controller())
        self.click_thread = threading.Thread(target=self.clicker.click, daemon=True)

        self.window = customtkinter.CTkToplevel()
        self.window.destroy()

    def popup(self, title="Error", message="Something went wrong."):
        if self.window.winfo_exists():
            self.window.focus()
            return

        self.window = customtkinter.CTkToplevel()
        self.window.title(title)
        self.window.geometry("300x100")
        self.window.resizable(False, False)

        customtkinter.CTkLabel(master=self.window, text=message, font=self.font_small).pack(pady=5)
        customtkinter.CTkButton(master=self.window, text="OK", command=self.window.destroy).pack(pady=5)

        self.window.focus()

    def setup_visuals(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        style = ttk.Style(self)
        self.tk.call("source", "assets/theme.tcl")
        style.theme_use("equilux")

        self.font_large = customtkinter.CTkFont(family='Comfortaa', size=25, weight='bold')
        self.font_medium = customtkinter.CTkFont(family='Comfortaa', size=17, weight='bold')
        self.font_small = customtkinter.CTkFont(family='Comfortaa', size=15)
        self.font_small_thick = customtkinter.CTkFont(family='Comfortaa', size=15, weight='bold')
        self.font_mini = customtkinter.CTkFont(family='Comfortaa', size=11)

    def setup_ui(self):
        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(pady=3, padx=3, fill="both", expand=True)

        customtkinter.CTkLabel(master=main_frame, text="AutoClicker", font=self.font_medium).pack(side="top")

        # Autoclicker select
        def autoclickerswitch_event(choice):
            if choice == "Keyboard":
                key_frame.lift()

            else:
                mouse_frame.lift()

        self.autoclicker_option = customtkinter.CTkOptionMenu(master=main_frame, values=["Mouse", "Keyboard"],
                                                              width=30, height=20, command=autoclickerswitch_event)
        self.autoclicker_option.pack(side="top", pady=3)


        # Mouse autoclicker frame, content
        mouse_frame = customtkinter.CTkFrame(master=main_frame, border_width=2, border_color="#3b3b3b")
        mouse_frame.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.5)

        mouse_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        mouse_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')

        # Clickspeedunitframe, content
        self.mousespeed_unit_choice = "CPS"

        def change_mousespeed_unit():
            if radio_var.get() == 1:
                self.mousespeed_unit_choice = "CPS"
                mouse_cps_frame.lift()

            else:
                self.mousespeed_unit_choice = "Interval"
                mouse_interval_frame.lift()

        radio_var = tkinter.IntVar(0)

        self.mousespeed_unit_option_cps = customtkinter.CTkRadioButton(master=mouse_frame, text="CPS", font=self.font_small_thick,
                                                        command=change_mousespeed_unit, variable=radio_var, value=1, radiobutton_width=11,
                                                                    radiobutton_height=11, border_width_checked=2, border_width_unchecked=2)
        self.mousespeed_unit_option_cps.select()

        self.mousespeed_unit_option_interval = customtkinter.CTkRadioButton(master=mouse_frame, text="Interval", font=self.font_small_thick,
                                                        command=change_mousespeed_unit, variable=radio_var, value=2, radiobutton_width=11,
                                                        radiobutton_height=11, border_width_checked=2, border_width_unchecked=2)

        self.mousespeed_unit_option_cps.grid(column=0, row=0, columnspan=3, rowspan=2)
        self.mousespeed_unit_option_interval.grid(column=2, row=0, columnspan=2, rowspan=2, stick="we")


        # CPS unit frame
        mouse_cps_frame = customtkinter.CTkFrame(master=mouse_frame, fg_color="#282928")
        mouse_cps_frame.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.4)

        customtkinter.CTkLabel(master=mouse_cps_frame, text="Clickspeed in CPS:", font=self.font_small_thick).pack(pady=2)

        self.mouse_cps_entry = customtkinter.CTkEntry(master=mouse_cps_frame, font=self.font_small, width=50)
        self.mouse_cps_entry.pack(pady=10)

        # Interval unit frame
        mouse_interval_frame = customtkinter.CTkFrame(master=mouse_frame, fg_color="#282928")
        mouse_interval_frame.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.4)
        mouse_interval_frame.lower()

        mouse_interval_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        mouse_interval_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        customtkinter.CTkLabel(master=mouse_interval_frame,
                               text="Clickspeed interval:", font=self.font_small_thick).grid(column=0, row=0, columnspan=3)

        customtkinter.CTkLabel(master=mouse_interval_frame, text="Minutes:", font=self.font_mini).grid(column=0, row=1)
        self.mouse_minute_entry = customtkinter.CTkEntry(master=mouse_interval_frame, font=self.font_mini, width=50)
        self.mouse_minute_entry.grid(column=0, row=1, rowspan=3, pady=19)
        self.mouse_minute_entry.insert(0, "0")

        customtkinter.CTkLabel(master=mouse_interval_frame, text="Seconds:", font=self.font_mini).grid(column=1, row=1)
        self.mouse_sec_entry = customtkinter.CTkEntry(master=mouse_interval_frame, font=self.font_mini, width=50)
        self.mouse_sec_entry.grid(column=1, row=1, rowspan=3, pady=19)
        self.mouse_sec_entry.insert(0, "0")

        customtkinter.CTkLabel(master=mouse_interval_frame, text="Milliseconds:", font=self.font_mini).grid(column=2, row=1)
        self.mouse_milsec_entry = customtkinter.CTkEntry(master=mouse_interval_frame, font=self.font_mini, width=50)
        self.mouse_milsec_entry.grid(column=2, row=1, rowspan=3, pady=19)
        self.mouse_milsec_entry.insert(0, "0")


        # Mbutton selection

        customtkinter.CTkLabel(master=mouse_frame, text="Select Mouse button:", font=self.font_small).grid(column=0, row=6,
                                                                            columnspan=2, rowspan=2, pady=2, padx=2)


        self.mbutton_select_optionmenu = customtkinter.CTkOptionMenu(master=mouse_frame,
                                                                values=["Left button", "Right button"], width=50, height=20)

        self.mbutton_select_optionmenu.grid(column=2, row=6, columnspan=2, rowspan=2, pady=2, sticky="w")



        # Key autoclicker frame, content
        key_frame = customtkinter.CTkFrame(master=main_frame, border_width=2, border_color="#3b3b3b")
        key_frame.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.5)
        key_frame.lower()


        customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=self.font_medium).pack()


        # Operating(start/stop) frame, content
        operating_frame = customtkinter.CTkFrame(master=main_frame)
        operating_frame.place(relx=0, rely=0.69, relwidth=1, relheight=0.31)


        ###operating_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        ###operating_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        def start_clicker():
            if self.clicker.running:
                return

            if self.mousespeed_unit_choice == "CPS":
                try:
                    self.clicker.interval = 1 / float(self.mouse_cps_entry.get())
                except:
                    self.popup(title="Error", message="Please enter a valid number.")
                    return
            else:
                try:
                    minutes = float(self.mouse_minute_entry.get()) * 60
                    seconds = float(self.mouse_sec_entry.get())
                    milliseconds = float(self.mouse_milsec_entry.get()) / 1000
                    self.clicker.interval = minutes + seconds + milliseconds
                except:
                    self.popup(title="Error", message="Please enter a valid number.")
                    return

            self.click_thread = threading.Thread(target=self.clicker.click, daemon=True)
            self.click_thread.start()


        # Start/Stop buttons
        start_button = customtkinter.CTkButton(master=operating_frame, text="Start (F5)", font=self.font_medium,
                                               border_color="#222222", border_width=3, command=start_clicker)
        start_button.place(relx=0.01, rely=0.02, relwidth=0.47, relheight=0.4)

        stop_button = customtkinter.CTkButton(master=operating_frame, text="Stop (F6)", font=self.font_medium,
                                              border_color="#222222", border_width=3, command=self.stop_clicker)
        stop_button.place(relx=0.52, rely=0.02, relwidth=0.47, relheight=0.4)

        # Operating Settings

    def stop_clicker(self):
        if not self.clicker.running:
            self.popup(title="Error", message="AutoClicker is not running.")
            return

        # TODO: add metrics
        self.clicker.running = False


if __name__ == "__main__":
    app = AutoClickerApp()
    app.mainloop()

    #threading.Thread(target=AutoClickerApp().mainloop).start()