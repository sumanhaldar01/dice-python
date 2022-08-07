import tkinter
from PIL import Image,ImageTk
import random
root=tkinter.Tk()
root.title('Dice Rolling Simulator')
root.geometry("500x300")
dice = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
img= ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tkinter.Label(root, image=img)
label1.image=img
label1.pack()
def roll():
    img= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=img)
    label1.image =img
b1=tkinter.Button(root,text="LET'S ROLL",bg='yellow',foreground='blue',command=roll)
b1.pack(expand=True)
root.mainloop()