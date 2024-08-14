from tkinter import *

window = Tk()  # Instantiate an instance of a window
window.geometry("420x420")  # Change the size of the window
window.title("First GUI program")  # Change the title

icon = PhotoImage(file='dog-house.png')
window.iconphoto(True, icon)  # Replace the icon
window.config(background="black")
window.mainloop()  # Place window on computer screen, listen for events
