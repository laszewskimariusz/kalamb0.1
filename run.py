#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
try:
    import Tkinter as tk # Python 2.x
except:
    import tkinter as tk # Python 3.x
 
import random
from pygame import mixer
import csv
 
#----------------------------------------------------------------------
 
LARGE_FONT = ("Verdana", 23)
PKT_FONT   = ("Verdana", 15)
 
#----------------------------------------------------------------------
 
class App(tk.Tk):
 
    def __init__(self):
        tk.Tk.__init__(self)
 
        self.title("kalambury 0.1")

        self.wm_iconbitmap("icon.ico")
 
        mixer.init(44100)
 
        self.clock = mixer.Sound("Ticking-clock.wav")
        self.alarm = mixer.Sound("alarm.wav")
 
        self.timer = None
 
        # --- wczytanie z CSV ---
 
        with open('hasla.txt') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            self.data = list(reader)
 
        #print self.data
 
        # --- naglowek ---
 
        tk.Label(self, text='Kalambury by Mariusz').grid(column=0, row=0, columnspan=3)
 
        # --- przyciski ---
 
        tk.Button(self, text="Losuj", height=8, width=15, bg="pink",
                    command=self.losuj).grid(column=0, row=3)
 
        tk.Button(self, text="Czas start", height=8, width=15, bg="pink",
                    command=lambda:self.countdown(60)).grid(column=2, row=3)
 
        # --- kategoria i haslo ---
 
        self.category = tk.StringVar()
 
        tk.Label(self, textvariable=self.category, wraplength=500, justify=tk.LEFT,
                    bg="blue", fg='ivory', font=LARGE_FONT,
                    width=50, height=5).grid(column=0, row=1, columnspan=3)
 
        self.subject = tk.StringVar()
 
        tk.Label(self, textvariable=self.subject, justify=tk.LEFT,
                    bg="blue", fg='ivory', font=LARGE_FONT,
                    width=50, height=5).grid(column=0, row=2, columnspan=3)
 
        # --- zegar ---
 
        self.time = tk.StringVar()
        self.time.set("00:00")
 
        tk.Label(self, textvariable=self.time, justify=tk.LEFT,
                    bg="blue", fg='ivory', font=LARGE_FONT, width=10,
                    height=5).grid(column=1, row=3)
 
        # --- inne ---
 
        self.losuj()
 
 
    def run(self):
        self.mainloop()
 
 
    def losuj(self):
        category, subject = random.choice(self.data)
        self.category.set('Kategoria: ' + category)
        self.subject.set('Hasło: ' + subject)
        #print(category, subject)
 
        # zatrzymanie odliczania
        if self.timer:
            self.after_cancel(self.timer)
            self.time.set("00:00")
 
 
    def countdown(self, left_time):
        self.time.set("00:{:02d}".format(left_time))
 
        if left_time == 13:
            self.clock.play()
        elif left_time == 1:
            self.alarm.play()
 
        if left_time > 0:
            self.timer = self.after(1000, self.countdown, left_time-1)
 
#----------------------------------------------------------------------
 
App().run()
