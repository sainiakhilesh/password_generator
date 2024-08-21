from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LABEL_FONT = "Impact"
WIDGET_FONT = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_data = web_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showwarning(title="Empty Field", message="Fields cannot be empty")
    else:
        is_ok = messagebox.askokcancel(title="website_data",
                                       message=f"These are the details entered: \nEmail: {email_data}"
                                               f"\nPassword: {password_data}")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website_data}|{email_data}|{password_data}\n")
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=(LABEL_FONT, 15))
web_label.config(pady=10, padx=10)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(LABEL_FONT, 15))
email_label.config(padx=10, pady=10)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(LABEL_FONT, 15))
password_label.config(padx=10,pady=10)
password_label.grid(column=0, row=3)

web_entry = Entry(width=35, font=(WIDGET_FONT, 10))
web_entry.insert(END, string="Enter Website Here")
web_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35,  font=(WIDGET_FONT, 10))
email_entry.insert(END,string="Enter Email/username here")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21, font=(WIDGET_FONT, 10))
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", font=(WIDGET_FONT, 10), width=10, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="ADD", font=(WIDGET_FONT, 10), width=36, padx=10, pady=10, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()