from tkinter import *
from tkinter import messagebox
import re

# Create the main application window
root = Tk()
root.title("Test Login Form")
root.geometry("2000x1000")
root.configure(bg="#d4d4d4")  # Set the background color of the main window

# Create the first frame with an increased vertical size
main_frame1 = Frame(root, borderwidth=0, relief="solid", highlightbackground="grey", highlightthickness=17)
main_frame1.place(x=370, y=0, width=800, height=650)
main_frame1.configure(bg="#d4d4d4")  # Set the background color of the first frame

# Create a label for the login page
Label(main_frame1, text="Login Page", bg="Teal", font="arial 40 bold", padx=10, pady=10).pack(pady=14)

# Create labels and entry fields for username and password
Label(main_frame1, text="Username:", fg="blue", font="arial 27 bold", bg="#d4d4d4").place(x=130, y=120)
entry1 = Entry(main_frame1, highlightbackground="#f4f4f4", highlightthickness=17, font="arial 27 bold")
entry1.place(x=321, y=104, relwidth=0.57)

Label(main_frame1, text="Password:", font="arial 27 bold", bg="#d4d4d4").place(x=134, y=201)
entry2 = Entry(main_frame1, bd=1, highlightbackground="#f4f4f4", highlightthickness=17, show="*", font="arial 27 bold")
entry2.place(x=321, y=185, relwidth=0.57)

# Create a frame for buttons
button_frame1 = Frame(main_frame1)
button_frame1.place(x=90, y=304)

# Function to handle login
def login():
    username = entry1.get()
    password = entry2.get()
    print(f"The value of username is: {entry1.get()}")
    print(f"The value of Password is: {entry2.get()}")
    # Validate username and password
    if username == "" and password == "":
        messagebox.showerror("Error", "Blank fields are not Allowed.")
    elif username == "":
        messagebox.showinfo("Error", "Please Enter Username.")
    elif password == "":
        messagebox.showinfo("Error", "Please Enter Password.")
    elif not re.search(r'[`~!@#$%^&*(),.?":{}|<>]', password):
        messagebox.showinfo("Error", "Password must contain Special Characters.")
    elif (username, password) in [("wali", "wali#"), ("User1", "Password!"), ("User2", "Password@")]:
        messagebox.showinfo("Success", "Login Successful")
       
    else:
        messagebox.showerror("Oops", "Invalid Username/Password")

# Create the login button
Button(button_frame1, text="Login", bd=17, padx=41, pady=0, command=login, font="arial 21 bold").pack(side=LEFT, padx=0.4)

# Function to reset fields
def reset():
    entry1.delete(0, "end")
    entry2.delete(0, "end")


# Function to exit window
def exit_window():
    root.destroy()

# Create the exit window button
Button(button_frame1, text="Exit Window", bd=17, padx=10, pady=0, command=exit_window, font="arial 21 bold").pack(side=LEFT)

# Create the reset button
Button(button_frame1, text="Reset", bd=17, padx=41, pady=0, command=reset, font="arial 21 bold").pack(side=LEFT, padx=7)




# Start the GUI event loop
root.mainloop()
