from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

def onLeave(event):
    btn.config(bg='#160bb3')


def onEnter(event):
    btn.config(bg='red')

color='#1d44b8'
window = Tk()
window.state('zoomed')

canvas = Canvas(window, bg=color, width=500, height=400, bd=0, highlightthickness=0, relief='ridge')
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
img = ImageTk.PhotoImage(Image.open("welcome.png"))
canvas.create_text(250, 50, fill="white", font="Times 45 bold", text="ONLINE TEST")
canvas.create_image(125, 130, anchor=NW, image=img)


myfont=font.Font(size=25)
btn = Button(window, text='ENTER', bd='2', bg='#160bb3', fg='white', width=259, height=104, relief='groove', borderwidth='2', cursor='hand2')
btn.place(relx=0.5, rely=0.85, anchor=CENTER, height=50, width=220)
btn.bind('<Leave>', onLeave)
btn.bind('<Enter>', onEnter)
btn['font']=myfont

window.title("Welcome")
window.configure(background=color)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry('%dx%d+0+0' %(width, height))
window.mainloop()