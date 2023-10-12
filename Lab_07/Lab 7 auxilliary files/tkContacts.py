print("Kanderi Guruteja")  # Student Name
print("Open source Programming-Python")  # Course name
print("Lab-07")  # Lab Number
print("Working with tkinter")  # Name of the Lab
print("A20526883")  # Student ID

# Import required modules
from tkinter import *
from tkinter import messagebox
import pickle
import os
import re
import time
from datetime import date
from myDatabasefile import *

# Check if the contacts.pickle file exists
if os.path.exists('contacts.pickle'):
    # contacts.pickle file for serialization and deserialization
    with open('contacts.pickle', 'rb') as f:
        contactlist1 = pickle.load(f)
else:
    # If contacts.pickle doesn't exist, load the contacts from contacts.py
    from contacts import contactlist

# Create the table in the database
create_table()

def selection():  # Function to get the selected index from the listbox
    selected_indices1 = select.curselection()
    if selected_indices1:
        return int(selected_indices1[0])
    else:
        return -1

def addContact():  # Function to add a new contact
    nameofcontact = nameVariable1.get()
    phoneofcontact = phone_Variables1.get()

    if nameofcontact and phoneofcontact:
        for contact in contactlist1:
            if contact[0] == nameofcontact:
                messagebox.showerror("Error", "Contact with the same name already exists.")
                return

        if not re.match("^[a-zA-Z0-9, -]+$", nameofcontact):
            messagebox.showerror("Error", "Invalid characters in the name. Please use only letters, numbers, hyphen, comma, or space.")
        elif not re.match("^[0-9-]+$", phoneofcontact) or len(phoneofcontact) < 10:
            messagebox.showerror("Error", "Invalid phone number. Please enter at least 10 digits and use only numbers and hyphen.")
        else:
            insert_contact(nameofcontact, phoneofcontact)
            contactlist1.append([nameofcontact, phoneofcontact])
            setList()
            saveContacts()
            messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Please enter a name and phone number.")

def updateContact():  # Function to update a contact
    selected_index = selection()
    if selected_index >= 0:
        name = nameVariable1.get()
        phone = phone_Variables1.get()
        if name and phone:
            if not re.match("^[a-zA-Z0-9,-]+$", name):
                messagebox.showerror("Error", "Invalid characters in the name. Please use only letters, numbers, hyphen, or comma.")
            else:
                contactlist1[selected_index] = [name, phone]
                update_contact(selected_index + 1, name, phone)  # Add +1 to selected_index to match the record ID in the database
                setList()
                saveContacts()
                messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact and load it before updating.")
    else:
        messagebox.showerror("Error", "No contact selected for update.")

def deleteContact():  # Function to delete a contact
    selected_index = selection()
    if selected_index >= 0:
        delete_contact(selected_index + 1)  # Add +1 to selected_index to match the record ID in the database
        del contactlist1[selected_index]
        setList()
        saveContacts()
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "No contact selected.")

def loadContact():  # Function to load a contact
    selected_index = selection()
    if selected_index >= 0:
        name, phone = contactlist1[selected_index]
        nameVariable1.set(name)
        phone_Variables1.set(phone)

def buildFrame():  # Function to build the GUI frame
    global nameVariable1, phone_Variables1, select
    root = Tk()
    root.title("My Contact List")

    frame1 = Frame(root)
    frame1.grid(row=0, column=0)
    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVariable1 = StringVar()
    name = Entry(frame1, textvariable=nameVariable1)
    name.grid(row=0, column=1, sticky=W)
    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phone_Variables1 = StringVar()
    phone = Entry(frame1, textvariable=phone_Variables1)
    phone.grid(row=1, column=1, sticky=W)

    frame2 = Frame(root)
    frame2.grid(row=1, column=0)
    btn1 = Button(frame2, text=" Add  ", command=addContact)
    btn1.grid(row=0, column=0, padx=5)
    btn2 = Button(frame2, text="Update", command=updateContact)
    btn2.grid(row=0, column=1, padx=5)
    btn3 = Button(frame2, text="Delete", command=deleteContact)
    btn3.grid(row=0, column=2, padx=5)
    btn4 = Button(frame2, text=" Load ", command=loadContact)
    btn4.grid(row=0, column=3, padx=5)
    btn5 = Button(frame2, text="Save", command=saveContacts)
    btn5.grid(row=0, column=4, padx=5)

    frame3 = Frame(root)
    frame3.grid(row=2, column=0, pady=10)
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=10)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH)

    btn6 = Button(root, text="Exit", command=exitProgram)
    btn6.grid(row=3, column=0, pady=10)

    return root

def setList():  # Function to update the listbox with the contact names
    contactlist1 = read_contacts()
    select.delete(0, END)
    for contact in contactlist1:
        select.insert(END, contact[1])

def saveContacts():
    with open('contacts.py', 'w') as f:
        f.write("contactlist = [\n")
        for contact in contactlist1:
            f.write(f"  ['{contact[0]}', '{contact[1]}'],\n")
        f.write("]\n")
    current_time = time.strftime("%H:%M:%S")
    current_date = date.today().strftime("%Y-%m-%d")
    messagebox.showinfo("Save", f"Contacts saved successfully.\nDate: {current_date}\nTime: {current_time}")


def exitProgram():
    if messagebox.askokcancel(title="Exit", message="Are you sure you want to exit?"):
        os._exit(1)

root = buildFrame()
setList()
root.protocol("WM_DELETE_WINDOW", exitProgram)
root.mainloop()
