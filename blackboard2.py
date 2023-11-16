# So this is my effort to make a simple blackboard. I haven't been crazy about any of my 
# programs (notes, kanban or todo). So maybe I'll pay attention if this is on my screen at startup.

from tkinter import *
import customtkinter
from datetime import datetime
import os
# import glob


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

main_window = customtkinter.CTk(className='GTBlackboard')
main_window.geometry("1500x950")
main_window.title("Grandpa Terry Simple Blackboard App")
icon = PhotoImage(file="blackboard.png")
main_window.iconphoto(True, icon)

def save_file():
    # Read file for the first time
    bb_file = open("blackboard.txt", "w")
    bb_file.write(content_box.get("1.0",END))
    bb_file.close()


def cancel():
    main_window.destroy()

# This is really going to just be a big text box with save and cancel buttons at the bottom.

# Text box for the user to make additional notes
text_box_font = customtkinter.CTkFont(family="whatever it takes", weight='bold', slant='italic', size=50)
content_box=customtkinter.CTkTextbox(main_window, wrap=WORD, font=text_box_font, text_color="#ffffff", fg_color="#343638")
content_box.place(relx=.005, rely=.03, relheight=.85, relwidth=.95)

# scrollbar=customtkinter.CTkScrollbar(main_window, command=content_box.yview)
# scrollbar.place(relx=.96, rely=.03, relheight=.85, relwidth=.02) #scrollbar
# content_box.configure(insertbackground = 'white')
# content_box.config(yscrollcommand=scrollbar.set)

# This button is bound to the function "save_file" which saves the file in the specified path'''
save_button=customtkinter.CTkButton(main_window, text="Save Card", font=("Ubuntu Regular", 24),
    command = save_file)
save_button.place(relx=.23, rely=0.92)

# Cancel Button 

cancel_button=customtkinter.CTkButton(main_window, text="Quit", font=("Ubuntu Regular", 24),
    command=cancel)
cancel_button.place(relx=.61, rely=0.92)

# Name of the data file is in blackboard.config and it's the only thing in that file.
config_file = open("blackboard.config", 'r')
data_file_name = config_file.read()
data_file_name = data_file_name.strip('\n') 
config_file.close()

# Read file for the first time
bb_file = open(data_file_name, "r")
bb_content = bb_file.read()
content_box.insert("1.0", bb_content)

main_window.mainloop()
