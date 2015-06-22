from tkinter import *
import random
from pygame import mixer
import time

Root = Tk()
RTitle = Root.title("kalambur.01")

Root.geometry("1280x720")
Root.wm_iconbitmap("icon.ico")
LARGE_FONT = ("Verdana", 23)
PKT_FONT =("Verdana", 15)

mixer.init(44100)

clock = mixer.Sound("Ticking-clock.wav")
alarm = mixer.Sound("alarm.wav")


class Puntkacja:





    def d_niebieska(self):
        pkt = '10'

        niebieska = Label(Root, text=("niebieska:"), wraplength=300, justify=LEFT, fg='blue', font=PKT_FONT, width=10, height=5)
        niebieska.grid(column=6, row=1)







class Timer:

    def countDown(self):
        for czas in range(60, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(czas, 120))
            time.sleep(1)
            if sf == '00:13':
                clock.play()
            if sf == '00:01':
                alarm.play()


            czas_okno = Label(Root, text=(sf), wraplength=300, justify=LEFT, bg="blue", fg='ivory', font=LARGE_FONT, width=10, height=5)
            czas_okno.grid(column=2, row=5)





            Root.update()



class Haslo:

    def losuj(self):

        self.line = random.choice(open('hasla.txt').readlines())
        okno = Label(Root, text=(self.line),wraplength=300, justify=LEFT, bg="blue", fg='ivory',font=LARGE_FONT, width=30, height=10)
        okno.grid(column=2, row=2)

        print(self.line)


class MainWindow(Haslo, Timer):


    def __init__(self, master):
        frame = Frame(master)
        frame.pack

        haslo = Haslo()
        haslo.losuj()

        odlicz = Timer()

        gracze = Puntkacja()
        gracze.d_niebieska()




        Label(text='Kalambury by Mariusz ').grid(column=4, row=0)
        Label(text='').grid(column=1, row=3, sticky=('n', 's'))

        Button(Root, text="Losuj", height=8, width=15, bg="pink", command=(self.losuj)).grid(column=5, row=2)
        Button(Root, text="Czas start", height=8, width=15, bg="pink", command=(odlicz.countDown)).grid(column=5, row=5)











app = MainWindow(Root)
Root.mainloop()