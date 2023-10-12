from tkinter import *

window = Tk()

def open_registration():
    window.destroy()
    from register import open_registration_window

def open_login():
    window.destroy()
    from login import open_login_window

def return_to_main():
    '''This function will allow the user to return to this window from another window'''
    pass


# Welcome message
welcome_label = Label(window, text="Welcome to Chart Analysis For Crime in Chicago", font=("Arial", 13))
welcome_label.pack(pady=(30, 10))  # Adjust the top and bottom padding

# Register button
registerBtn = Button(window, text="Register", width=30, height=2, command=open_registration)
registerBtn.pack(pady=10)

# Login button
loginBtn = Button(window, text="Login", width=30, height=2, command=open_login)
loginBtn.pack(pady=10)

# Set the window dimensions and position
window_width = 440
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 8
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


# window configs
window.title("Chart Analysis For Crime in Chicago")
window.geometry("440x440")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
