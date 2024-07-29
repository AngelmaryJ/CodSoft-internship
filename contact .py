from tkinter import *

def save_data():
    nametext = Name.get()
    phonetext = Phone.get()
    with open('contacts.txt','a') as file:
        file.write(f"Name : {nametext}\n")
        file.write(f"Phone : {phonetext}\n\n")

    Label(root, text="contact saved successfully", fg='green').grid(row=4, column=1)
    Name.set('')
    Phone.set('')
root = Tk()
root.geometry('400x400')

#labels
Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=10)

#variables
Name = StringVar()
Phone = StringVar()

#entries
Entry(root, textvariable=Name).grid(row=0, column=1, pady=10)
Entry(root, textvariable=Phone).grid(row=1, column=1, pady=10)

#button
Button(root, text="submit", command=save_data).grid(row=3, column=1)
root.mainloop()

