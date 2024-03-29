import tkinter
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

        self.geometry('300x375')
        self.resizable(False, False)
        self.title("AutoClicker")
        self.option_add("*tearOff", False)

        self.clicker = Clicker(1, Controller())
        self.click_thread = threading.Thread(target=self.clicker.click, daemon=True)

        self.setup_visuals()
        self.setup_ui()

        self.window = customtkinter.CTkToplevel()
        self.window.destroy()

        self.settings_window = customtkinter.CTkToplevel()
        self.settings_window.destroy()

        self.stats_window = customtkinter.CTkToplevel()
        self.stats_window.destroy()

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

        self.icon_histogram = customtkinter.CTkImage(Image.open("assets/histogram.png"), size=(20, 20))
        self.icon_settings = customtkinter.CTkImage(Image.open("assets/settings-icon.png"), size=(25, 25))

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
        mouse_frame.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.54)

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

        mouse_cps_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
        mouse_cps_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

        customtkinter.CTkLabel(master=mouse_cps_frame, text="Clickspeed in CPS:", font=self.font_small_thick).grid(column=0, row=0, columnspan=3)

        self.mouse_cps_entry = customtkinter.CTkEntry(master=mouse_cps_frame, font=self.font_small, width=50)
        self.mouse_cps_entry.grid(column=1, row=1, rowspan=3, pady=19)

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
        key_frame.place(relx=0.01, rely=0.18, relwidth=0.98, relheight=0.54)
        key_frame.lower()


        customtkinter.CTkLabel(master=key_frame, text="Keyboard", font=self.font_medium).pack()


        # Operating(start/stop) frame, content
        operating_frame = customtkinter.CTkFrame(master=main_frame)
        operating_frame.place(relx=0, rely=0.74, relwidth=1, relheight=0.3)


        def start_clicker():
            self.start_button.configure(state=DISABLED)
            self.stop_button.configure(state=NORMAL)
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
        self.hotkey_start = "f2"#self.clicker.start_key.name.upper() if hasattr(self.clicker.start_key, 'name') else str(self.clicker.start_key)
        self.hotkey_stop = "f3"#self.clicker.stop_key.name.upper() if hasattr(self.clicker.stop_key, 'name') else str(self.clicker.stop_key)

        self.start_button = customtkinter.CTkButton(master=operating_frame, text=f"Start ({self.hotkey_start})", font=self.font_medium,
                                               border_color="#222222", border_width=3, command=start_clicker)
        self.start_button.place(relx=0.01, rely=0.35, relwidth=0.47, relheight=0.45)

        self.stop_button = customtkinter.CTkButton(master=operating_frame, text=f"Stop ({self.hotkey_stop})", font=self.font_medium,
                                              border_color="#222222", border_width=3, command=self.stop_clicker, state=DISABLED)
        self.stop_button.place(relx=0.52, rely=0.35, relwidth=0.47, relheight=0.45)


        # Delay slider
        customtkinter.CTkLabel(master=operating_frame, text="Set start delay:", font=self.font_small_thick).place(relx=0.02, rely=0.05)

        def startdelay_display_update(value):
            self.startdelay_display.configure(text=f"{value}s")
            self.startdelay = value

        self.startdelay_display = customtkinter.CTkLabel(master=operating_frame, text="0.0s", font=self.font_small)
        self.startdelay_display.place(relx=0.4, rely=0.05)

        self.startdelay = 0

        self.startdelay_slider = customtkinter.CTkSlider(master=operating_frame, from_=0, to=15, number_of_steps=15,
                                                          command=startdelay_display_update)

        self.startdelay_slider.place(relx=0.55, rely=0.11, relwidth=0.45)
        self.startdelay_slider.set(0)


        # Settings


        def open_settings_window():

            if self.settings_window.winfo_exists():
                self.settings_window.focus()
                return

            self.settings_window = customtkinter.CTkToplevel()
            self.settings_window.title("Settings")
            self.settings_window.geometry("250x300")
            self.settings_window.resizable(False, False)

            customtkinter.CTkLabel(master=self.settings_window, text="Settings", font=self.font_large).pack(pady=10)

            # Settings for Hotkeys
            settings_hotkey_frame = customtkinter.CTkFrame(master=self.settings_window, fg_color="#3b3b3b", height=300)
            settings_hotkey_frame.pack(pady=5, padx=8, fill=X)

            settings_hotkey_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
            settings_hotkey_frame.rowconfigure((0, 1, 2, 3), weight=1, uniform='a')

            customtkinter.CTkLabel(master=settings_hotkey_frame, text="Hotkeys", font=self.font_medium).grid(column=0, row=0, columnspan=3)
            hotkey_window_info = customtkinter.CTkLabel(master=settings_hotkey_frame, text="Click to change", font=self.font_small)
            hotkey_window_info.grid(column=0, row=1, columnspan=3)
            customtkinter.CTkLabel(master=settings_hotkey_frame, text="Start:", font=self.font_small_thick).grid(column=0, row=2, columnspan=2)
            customtkinter.CTkLabel(master=settings_hotkey_frame, text="Stop:", font=self.font_small_thick).grid(column=0, row=3, columnspan=2)
            # Hotkey change logic
            def change_start_hotkey(filler):
                hotkey_window_info.configure(text="Recording, press ESC to cancel")
                self.settings_window.update()
                start_hotkey_entry.configure(state=NORMAL)
                start_hotkey_entry.delete(0, END)
                with keyboard.Events() as events:
                    for event in events:
                        if event.key == keyboard.Key.esc or format(event.key).strip("Key.'").upper() == self.hotkey_stop:
                                start_hotkey_entry.insert(0, self.hotkey_start)
                                start_hotkey_entry.configure(state=DISABLED)
                                hotkey_window_info.configure(text="Click to change")
                                break
                        else:
                            self.clicker.update_start_key(event.key)
                            self.hotkey_start = format(event.key).strip("Key.'").upper()
                            start_hotkey_entry.insert(0, self.hotkey_start)
                            start_hotkey_entry.configure(state=DISABLED)
                            hotkey_window_info.configure(text="Click to change")
                            self.start_button.configure(text=f"Start ({self.hotkey_start})")
                            break

            def change_stop_hotkey(filler):
                hotkey_window_info.configure(text="Recording, press ESC to cancel")
                self.settings_window.update()
                stop_hotkey_entry.configure(state=NORMAL)
                stop_hotkey_entry.delete(0, END)
                with keyboard.Events() as events:
                    for event in events:
                        if event.key == keyboard.Key.esc or format(event.key).strip("Key.'").upper() == self.hotkey_start:
                            stop_hotkey_entry.insert(0, self.hotkey_stop)
                            stop_hotkey_entry.configure(state=DISABLED)
                            hotkey_window_info.configure(text="Click to change")
                            break
                        else:
                            self.clicker.update_stop_key(event.key)
                            self.hotkey_stop = format(event.key).strip("Key.'").upper()
                            stop_hotkey_entry.insert(0, self.hotkey_stop)
                            stop_hotkey_entry.configure(state=DISABLED)
                            hotkey_window_info.configure(text="Click to change")
                            self.stop_button.configure(text=f"Stop ({self.hotkey_stop})")
                            break


            start_hotkey_entry = customtkinter.CTkEntry(master=settings_hotkey_frame, font=self.font_small_thick, width=60)
            start_hotkey_entry.insert(0, self.hotkey_start)
            start_hotkey_entry.bind("<1>", change_start_hotkey)

            stop_hotkey_entry = customtkinter.CTkEntry(master=settings_hotkey_frame, font=self.font_small_thick, width=60)
            stop_hotkey_entry.insert(0, self.hotkey_stop)
            stop_hotkey_entry.bind("<1>", change_stop_hotkey)

            start_hotkey_entry.grid(column=1, row=2, columnspan=2)
            stop_hotkey_entry.grid(column=1, row=3, columnspan=2)



            customtkinter.CTkButton(master=self.settings_window, text="Save", command=self.settings_window.destroy).pack()
            self.settings_window.focus()


        open_settings_button = customtkinter.CTkButton(master=main_frame, image=self.icon_settings, text="", fg_color="#3b3b3b", hover_color="#636363",
                                                    command=open_settings_window)
        open_settings_button.place(relx=0.85, rely=0.01, relwidth=0.13, relheight=0.08)


        # Overall stats interface
        def open_stats_window():
            if self.stats_window.winfo_exists():
                self.stats_window.focus()
                return

            self.stats_window = customtkinter.CTkToplevel()
            self.stats_window.title("Overall Stats")
            self.stats_window.geometry("250x300")
            self.stats_window.resizable(False, False)


            customtkinter.CTkLabel(master=self.stats_window, text="Overall stats", font=self.font_large).pack(pady=15)

            # Stats:
            stat_1 = customtkinter.CTkFrame(master=self.stats_window, fg_color="#3b3b3b")
            stat_1.pack(pady=5, padx=8, fill=X)
            customtkinter.CTkLabel(master=stat_1, text="Statlongschlong 1:", font=self.font_medium).pack(side = LEFT, padx=5)
            customtkinter.CTkLabel(master=stat_1, text="value", font=self.font_small).pack(side=RIGHT, padx=10)

            stat_2 = customtkinter.CTkFrame(master=self.stats_window, fg_color="#3b3b3b")
            stat_2.pack(pady=3, padx=8, fill=X)
            customtkinter.CTkLabel(master=stat_2, text="Statlongschlong 2:", font=self.font_medium).pack(side=LEFT, padx=5)
            customtkinter.CTkLabel(master=stat_2, text="value", font=self.font_small).pack(side=RIGHT, padx=10)



            self.stats_window.focus()



        stats_open_button = customtkinter.CTkButton(master=main_frame, image=self.icon_histogram, text="", font=self.font_small, fg_color="#3b3b3b",
                                                     hover_color="#636363", command=open_stats_window)
        stats_open_button.place(relx=0.02, rely=0.01, relwidth=0.13, relheight=0.08)




    def stop_clicker(self):
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)

        # TODO: add metrics
        self.clicker.running = False


if __name__ == "__main__":
    app = AutoClickerApp()
    app.mainloop()

    #threading.Thread(target=AutoClickerApp().mainloop).start()