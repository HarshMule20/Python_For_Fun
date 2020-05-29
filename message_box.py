import tkinter
from tkinter import messagebox

# creating an object
top = tkinter.Tk()
top.geometry("75x75")

# to show info message_box
tkinter.messagebox.showinfo("info", "This is information")

# to show warning message box
tkinter.messagebox.showwarning("warning", "Hey! this is a warning")

# to show error message box
tkinter.messagebox.showerror("error", "Hey! I just caught an error")
top.mainloop()
