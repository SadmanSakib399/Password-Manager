import sys
import os
import random
import pyperclip
import json
from tkinter import *
from tkinter import messagebox

# RESOURCE PATH FOR .EXE COMPATIBILITY
def resource_path(relative_path):
    """For bundled files like images"""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def local_data_path(filename):
    """For saving user-generated files like passwords.json"""
    base_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    return os.path.join(base_path, filename)

# VARIABLES
NUMBERS = list("0123456789")
SYMBOLS = list(r"!@#$%^&*()-_=+[{]}\\|;:',<.>/?`~")
LOWERCASE_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
UPPERCASE_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ENTRY_INPUT_FONT = ("Arial", 14, "bold")
TEXT_COLOR = "#9ABFD0"
INPUT_BACKGROUND_COLOR = "#3B4255"

empty_status = None
empty_status_timer = None
default_Email = None

# FUNCTIONS
def status_msg(status, time=2000):
    global empty_status, empty_status_timer
    if empty_status_timer:
        canvas.after_cancel(empty_status_timer)
        empty_status_timer = None
    if empty_status:
        canvas.delete(empty_status)
        empty_status = None
    empty_status = canvas.create_text(450, 375, text=status, fill=TEXT_COLOR, font=("Arial", 16, "bold"))
    empty_status_timer = canvas.after(time, clear_status_message)

def clear_status_message():
    global empty_status, empty_status_timer
    if empty_status:
        canvas.delete(empty_status)
        empty_status = None
    empty_status_timer = None

def password_generate(numbers=NUMBERS, symbols=SYMBOLS, lowercase_letters=LOWERCASE_LETTERS, uppercase_letters=UPPERCASE_LETTERS):
    characters = []
    website_password.delete(0, END)
    times = var.get()
    for _ in range(times):
        characters.append(random.choice(numbers))
        characters.append(random.choice(symbols))
        characters.append(random.choice(lowercase_letters))
        characters.append(random.choice(uppercase_letters))
    random.shuffle(characters)
    generated_password = ''.join(characters)
    website_password.insert(0, generated_password)
    status_msg(f"{4 * times} Character Password Generated")
    pyperclip.copy(generated_password)

def add_password():
    website = website_name.get().capitalize()
    email = website_email.get()
    password = website_password.get()
    new_data = {website: {"Email": email, "Password": password}}

    if not website or not email or not password:
        status_msg("Please fill in all fields.")
        return

    sure = messagebox.askokcancel(title="Password Manager", message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n\nSave these details?")
    if sure:
        try:
            with open(local_data_path("passwords.json"), "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        data.update(new_data)
        with open(local_data_path("passwords.json"), "w") as file:
            json.dump(data, file, indent=4)
        website_name.delete(0, END)
        website_email.delete(0, END)
        website_password.delete(0, END)
        status_msg("Details Added Successfully.")

def search():
    website = website_name.get().capitalize()
    try:
        with open(local_data_path("passwords.json"), "r") as file:
            data = json.load(file)
            if website in data:
                status_msg("Website Found")
                website_email.delete(0, END)
                website_password.delete(0, END)
                website_email.insert(0, data[website]["Email"])
                website_password.insert(0, data[website]["Password"])
            else:
                status_msg("No Website Found")
    except FileNotFoundError:
        status_msg("File not Found")

def clear_all():
    status_msg("All Cleared")
    website_name.delete(0, END)
    website_email.delete(0, END)
    website_password.delete(0, END)

def default():
    email = website_email.get()
    with open(local_data_path("email.txt"), "w") as dmail:
        dmail.write(email)

def insert_default():
    try:
        with open(local_data_path("email.txt"), "r") as email:
            mail = email.read()
            return mail
    except FileNotFoundError:
        return ""

def set_reset_default():
    email = website_email.get()
    ask = messagebox.askyesnocancel(
        title="Default email",
        message=f"Do you want to save this email as default:\n\n{email}\n\n\nPress YES to set as default,\nPress NO to delete previous default,\nPress CANCEL to do nothing."
    )
    if ask == True:
        default()
        insert_default()
        status_msg("Email saved as default")
    elif ask == False:
        with open(local_data_path("email.txt"), "w") as dmail:
            dmail.write("")
        status_msg("Default email reset")

# UI SETUP
window = Tk()
window.title("Password Manager")
window.resizable(False, False)

canvas = Canvas(width=900, height=620)
logo_img = PhotoImage(file=resource_path("lock_logo.png"))
canvas.create_image(450, 200, image=logo_img)
canvas.config(bg="#1E222D")
canvas.grid()

canvas.create_text(255, 415, text="Website:", fill=TEXT_COLOR, font=("Arial", 16, "bold"))
canvas.create_text(210, 455, text="Email / Username:", fill=TEXT_COLOR, font=("Arial", 16, "bold"))
canvas.create_text(247, 495, text="Password:", fill=TEXT_COLOR, font=("Arial", 16, "bold"))

website_name = Entry(font=ENTRY_INPUT_FONT, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR)
website_email = Entry(font=ENTRY_INPUT_FONT, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR)
website_password = Entry(font=ENTRY_INPUT_FONT, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR)
website_name.place(x=325, y=400, width=250, height=30)
website_email.place(x=325, y=440, width=362, height=30)
website_password.place(x=325, y=480, width=250, height=30)
website_name.focus()
website_email.insert(0, insert_default())

password_generate_button = Button(text="Generate Password", width=18, bg="#1E222D", fg=TEXT_COLOR, font=("Arial", 10, "bold"), command=password_generate)
password_generate_button.place(x=582, y=482)

add_button = Button(text="Add", width=24, bg="#1E222D", fg=TEXT_COLOR, font=("Arial", 12, "bold"), command=add_password)
add_button.place(x=325, y=520)

search_button = Button(text="Search", width=18, bg="#1E222D", fg=TEXT_COLOR, font=("Arial", 10, "bold"), command=search)
search_button.place(x=582, y=402)

clear_all_button = Button(text="Clear All", width=10, bg="#1E222D", fg=TEXT_COLOR, font=("Arial", 12, "bold"), command=clear_all)
clear_all_button.place(x=190, y=520)

default_button = Button(text="💾", bg="#1E222D", fg=TEXT_COLOR, font=("Arial", 14, "bold"), command=set_reset_default)
default_button.place(x=695, y=436)

var = IntVar()
var.set(4)
r1 = Radiobutton(text="12", variable=var, value=3, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"), selectcolor="#1E222D")
r2 = Radiobutton(text="16", variable=var, value=4, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"), selectcolor="#1E222D")
r3 = Radiobutton(text="20", variable=var, value=5, bg=INPUT_BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"), selectcolor="#1E222D")
r1.place(x=580, y=520)
r2.place(x=635, y=520)
r3.place(x=690, y=520)

window.mainloop()
