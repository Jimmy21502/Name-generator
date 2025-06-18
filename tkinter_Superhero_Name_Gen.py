import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = "Arial 14 bold"

def font():
    if darkmode_var.get() == 1:
        root.configure(bg = "black")
    else:
        root.configure(bg = "#d9d9d9")

top_frame = tk.Frame(root)
top_frame.pack(fill="x")

title = tk.Label(top_frame, text = "Hero name generator", bg = "purple", font = style, fg = "white")
title.pack(fill = "x")

adjective_label = tk.Label(root, text = "Choose an adjective...", font = style)
adjective_label.pack(pady = 10)

ADJECTIVE1 = "Happy"
ADJECTIVE2 = "Awesome"
ADJECTIVE3 = "Outgoing"
ADJECTIVE4 = "Funky"

        

def radio_call():
    global adjective
    if adjective_var.get() == "happy":
        adjective = "Happy"
    elif adjective_var.get() == "awesome":
        adjective = "Awesome"
    elif adjective_var.get() == "outgoing":
        adjective = "Outgoing"
    elif adjective_var.get() == "funky":
        adjective = "Funky"
    return adjective

def generator():
    name = f"You are the {adjective} {colour_entrybox.get().title()} {chosen_animal.get()}!"
    hero_name_label.config(text = name)
    
adjective_var = tk.StringVar()

happy_radio = ttk.Radiobutton(root, text = "Happy", variable = adjective_var, value = "happy", command = radio_call)
happy_radio.pack()

awesome_radio = ttk.Radiobutton(root, text = "Awesome", variable = adjective_var, value = "awesome", command = radio_call)
awesome_radio.pack()

outgoing_radio = ttk.Radiobutton(root, text = "Outgoing", variable = adjective_var, value = "outgoing", command = radio_call)
outgoing_radio.pack()

funky_radio = ttk.Radiobutton(root, text = "Funky", variable = adjective_var, value = "funky", command = radio_call)
funky_radio.pack()

colour_label = tk.Label(root, text = "Enter a colour", font = style)
colour_label.pack(pady = 10)

colour_entrybox = tk.Entry(root, width = 27)
colour_entrybox.pack()

animal_label = tk.Label(root, text = "Pick an animal", font = style)
animal_label.pack(pady = 10)

animals_list = ["Dog", "Cat", "Unicorn"]
chosen_animal = tk.StringVar()
chosen_animal.set("")
animal_combobox = ttk.Combobox(root, textvariable = chosen_animal, state = "readonly", width = 24)
animal_combobox['values'] = animals_list
animal_combobox.pack()

go_button = tk.Button(root, text = "GO!", font = style, command = generator, width = 9)
go_button.pack(pady = 20)

hero_name_label = tk.Label(root, font = style, text = "", fg = "purple")
hero_name_label.pack()

darkmode_var = tk.IntVar()
darkmode_var.set(0)
darkmode = ttk.Checkbutton(root, text = "Dark mode", variable = darkmode_var, command = font)
darkmode.pack()

root.mainloop()