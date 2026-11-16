
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Right Click Menu Example")
root.geometry("500x500")


# Menu commands
def hello():
    messagebox.showinfo("Hello", "Hello!")


def goodbye():
    messagebox.showinfo("Goodbye", "Goodbye!")


# Display right-click menu
def show_menu(event):
    try:
        my_menu.tk_popup(event.x_root, event.y_root)
    finally:
        my_menu.grab_release()


# Create popup menu
my_menu = Menu(root, tearoff=0)

my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Good-bye", command=goodbye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.destroy)


# Bind right mouse button
root.bind("<Button-3>", show_menu)

root.mainloop()
