import tkinter
import tkinter as tk
import tkinter.font as font
import customtkinter
import threading


from tkinter import *
from tkinter import ttk
from clicker import Clicker
from pynput.mouse import Controller, Button
from pynput import keyboard
from PIL import Image, ImageTk


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

        self.hotkey_window = customtkinter.CTkToplevel()
        self.hotkey_window.destroy()

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

        self.icon_histogram = ImageTk.PhotoImage(Image.open("assets/histogram.png").resize((20,20)))

    def setup_ui(self):
        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(pady=3, padx=3, fill="both", expand=True)

        customtkinter.CTkLabel(master=main_frame, text="AutoClicker", font=self.font_large).pack(side="top")

        # Autoclicker select
        def autoclickerswitch_event(choice):
            if choice == "Keyboard":
                key_frame.lift()

            else:
                mouse_frame.lift()

        self.autoclicker_option = customtkinter.CTkOptionMenu(master=main_frame, values=["Mouse", "Keyboard"],
                                                              width=40, height=25, command=autoclickerswitch_event)
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
        self.mousespeed_unit_option_interval.grid(column=2, row=0, columnspan=2, rowspan=2, stick="w")


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

        ## Operating Settings

        # Delay slider
        customtkinter.CTkLabel(master=operating_frame, text="Set start delay:", font=self.font_small_thick).place(relx=0.02, rely=0.5)

        def startdelay_display_update(value):
            self.startdelay_display.configure(text=f"{value}s")
            self.startdelay = value

        self.startdelay_display = customtkinter.CTkLabel(master=operating_frame, text="0.0s", font=self.font_small)
        self.startdelay_display.place(relx=0.4, rely=0.5)

        self.startdelay = 0

        self.startdelay_slider = customtkinter.CTkSlider(master=operating_frame, from_=0, to=15, number_of_steps=15,
                                                          command=startdelay_display_update)

        self.startdelay_slider.place(relx=0.01, rely=0.75, relwidth=0.45)
        self.startdelay_slider.set(0)


        # Change Hotkey button
        self.hotkey_start = "F5"
        self.hotkey_stop = "F6"


        def change_hotkey_popup():

            if self.hotkey_window.winfo_exists():
                self.hotkey_window.focus()
                return


            self.hotkey_window = customtkinter.CTkToplevel()
            self.hotkey_window.title("Start/Stop Hotkeys")
            self.hotkey_window.geometry("300x100")
            self.hotkey_window.resizable(False, False)

            customtkinter.CTkLabel(master=self.hotkey_window, text="Start", font=self.font_small_thick).place(relx=0.1, rely=0.15,
                                                                                                 relwidth=0.25, relheight=0.2)
            customtkinter.CTkLabel(master=self.hotkey_window, text="Stop", font=self.font_small_thick).place(relx=0.65, rely=0.15,
                                                                                                relwidth=0.25, relheight=0.2)
            # Hotkey change logic
            def change_start_hotkey(filler):
                hotkey_window_info.configure(text="Recording, press ESC to cancel")
                start_hotkey_entry.configure(state=NORMAL)
                start_hotkey_entry.delete(0, END)
                self.hotkey_window.update()
                with keyboard.Events() as events:
                    for event in events:
                        if isinstance(event, keyboard.Events.Press):
                            if event.key == keyboard.Key.esc or format(event.key).strip("Key.'").upper() == self.hotkey_stop:
                                start_hotkey_entry.insert(0, self.hotkey_start)
                                start_hotkey_entry.configure(state=DISABLED)
                                hotkey_window_info.configure(text="Click to change")
                                break
                            self.hotkey_start = format(event.key).strip("Key.'").upper()
                            start_hotkey_entry.insert(0, self.hotkey_start)
                            start_hotkey_entry.configure(state=DISABLED)
                            hotkey_window_info.configure(text="Click to change")
                            start_button.configure(text=f"Start ({self.hotkey_start})")
                            break

            def change_stop_hotkey(filler):
                hotkey_window_info.configure(text="Recording, press ESC to cancel")
                stop_hotkey_entry.configure(state=NORMAL)
                stop_hotkey_entry.delete(0, END)
                self.hotkey_window.update()
                with keyboard.Events() as events:
                    for event in events:
                        if isinstance(event, keyboard.Events.Press):
                            if event.key == keyboard.Key.esc or format(event.key).strip("Key.'").upper() == self.hotkey_start:
                                stop_hotkey_entry.insert(0, self.hotkey_stop)
                                stop_hotkey_entry.configure(state=DISABLED)
                                hotkey_window_info.configure(text="Click to change")
                                break
                            self.hotkey_stop = format(event.key).strip("Key.'").upper()
                            stop_hotkey_entry.insert(0, self.hotkey_stop)
                            stop_hotkey_entry.configure(state=DISABLED)
                            hotkey_window_info.configure(text="Click to change")
                            stop_button.configure(text=f"Stop ({self.hotkey_stop})")
                            break


            start_hotkey_entry = customtkinter.CTkEntry(master=self.hotkey_window, font=self.font_small_thick)
            start_hotkey_entry.insert(0, self.hotkey_start)
            start_hotkey_entry.bind("<1>", change_start_hotkey)

            stop_hotkey_entry = customtkinter.CTkEntry(master=self.hotkey_window, font=self.font_small_thick)
            stop_hotkey_entry.insert(0, self.hotkey_stop)
            stop_hotkey_entry.bind("<1>", change_stop_hotkey)

            start_hotkey_entry.place(relx=0.15, rely=0.35, relwidth=0.15, relheight=0.2)
            stop_hotkey_entry.place(relx=0.7, rely=0.35, relwidth=0.15, relheight=0.2)

            hotkey_window_info = customtkinter.CTkLabel(master=self.hotkey_window, text="Click to change", font=self.font_small,
                                                        wraplength=110, justify="center")
            hotkey_window_info.pack(pady=16)

            customtkinter.CTkButton(master=self.hotkey_window, text="Save", command=self.hotkey_window.destroy()).place(relx=0.375, rely=0.7,
                                                                                                     relwidth=0.25, relheight=0.2)
            self.hotkey_window.focus()


        change_hotkey_button = customtkinter.CTkButton(master=operating_frame, text="Change Hotkeys", font=self.font_medium,
                                                       fg_color="#3b3b3b", hover_color="#636363",
                                                       border_color="#222222", border_width=3, command=change_hotkey_popup)
        change_hotkey_button.place(relx=0.52, rely=0.5, relwidth=0.47, relheight=0.4)

        # Overall stats interface
        stats_open_button = customtkinter.CTkButton(master=main_frame, image=self.icon_histogram, text="", fg_color="#3b3b3b", width=20)
        stats_open_button.place(relx=0.02, rely=0.01)




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