from tkinter import *
import random

import time

Root = Tk()
RTitle = Root.title("kalambur.01")

Root.geometry("1280x720")
Root.wm_iconbitmap("icon.ico")
LARGE_FONT = ("Verdana", 23)



class Timer:

    def countDown(self):
        for czas in range(60, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(czas, 120))
            time.sleep(1)

            czas_okno = Label(Root, text=(sf), wraplength=300, justify=LEFT, bg="blue", fg='ivory', font=LARGE_FONT, width=10, height=5)
            czas_okno.grid(column=2, row=5)
            Root.update()



class Haslo:

    def losuj(self):

        self.line = random.choice(open('hasla.txt').readlines())
        okno = Label(Root, text=(self.line),wraplength=300, justify=LEFT, bg="blue", fg='ivory',font=LARGE_FONT, width=50, height=10)
        okno.grid(column=2, row=2)

        print(self.line)


class MainWindow(Haslo, Timer):


    def __init__(self, master):
        frame = Frame(master)
        frame.pack

        haslo = Haslo()
        haslo.losuj()

        odlicz = Timer()
      # odlicz.countDown()



        Label(text='Kalambury by Mariusz ').grid(column=4, row=0)
        Label(text='').grid(column=1, row=3, sticky=('n', 's'))
        Label(text='Haslo').grid(column=2, row=1)
        Button(Root, text="Losuj", height=8, width=15, bg="pink", command=(self.losuj)).grid(column=6, row=2)
        Button(Root, text="Czas start", height=8, width=15, bg="pink", command=(odlicz.countDown)).grid(column=6, row=5)











app = MainWindow(Root)
Root.mainloop()