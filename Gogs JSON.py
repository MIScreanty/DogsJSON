import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title("Dogs JSON")
window.geometry("500x400")

i_m = Label(window)
i_m.pack()

btn = Button(window, text="Get dog image")
btn.pack()

window.mainloop()