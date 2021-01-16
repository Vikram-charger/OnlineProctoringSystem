from tkinter import *
from PIL import Image, ImageTk
import cv2

#Set up GUI
window = Tk()  #Makes main window
window.wm_title("Online Test Portal")
window.config(background="#E0EEEE")
window.state('zoomed')

#Graphics window
imageFrame = Frame(window)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)



#Slider window (slider controls stage position)
sliderFrame = Frame(window, width=600, height=100)
sliderFrame.grid(row=600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI


