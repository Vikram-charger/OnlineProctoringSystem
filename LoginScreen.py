from tkinter import *

from PIL import ImageTk, Image

bgColor = '#00E5EE'

loginWindow=Tk() #creating window object
loginWindow.state('zoomed')
#creating canvas
canvas = Canvas(
    loginWindow,
    bg='#FFFF66',
    width=400,
    height=600,
    relief='groove',
    bd=0,
    highlightthickness=0
    )
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

#widgets over canvas
img = ImageTk.PhotoImage(Image.open("img/login.png"))
canvas.create_image(100, 50, anchor=NW,image=img)
# canvas.create_text(200, 175, font=("Helvetica", 36, "bold", "underline"), text="LOGIN")
#Entry
userName = Entry(loginWindow, bd=0, font=("Arial", 10, "bold"), fg='white', bg='#696969', justify=CENTER)
passWord = Entry(loginWindow, bd=0, font=("Arial", 10, "bold"), fg='white', bg='#696969', justify=CENTER, show='*')
canvas.create_text(200, 279, text='Username', font=("Times", 15))
canvas.create_window(200, 310, window=userName, width=220, height=30)
canvas.create_text(200, 360, text='Password', font=("Times", 15))
canvas.create_window(200, 390, window=passWord, width=220, height=30)
#LoginButton
loginPhoto = PhotoImage(file="img/key.png")
button = Button(loginWindow, image=loginPhoto, width=200, height=50, cursor="hand2")
canvas.create_window(200, 480, window=button)
#Login Window Properties
loginWindow.title("Welcome")
loginWindow.configure(background=bgColor)
width = loginWindow.winfo_screenwidth()
height = loginWindow.winfo_screenheight()
loginWindow.geometry('%dx%d+0+0' %(width, height))
loginWindow.mainloop()