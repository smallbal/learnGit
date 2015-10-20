__author__ = 'guest_zjr'
# !/usr/bin/env python3
# -*-coding:utf-8-*-

from tkinter import *
import random
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Run and Fucking escape!")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0,5):
            for y in range(0,5):
                self.canvas.create_image(x*w, y*h, image=self.bg, anchor='nw')
        self.sprites = []  # sprite:精灵
        self.running = True

    def mainloop(self):
        while True:
            if self.running:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)


# 坐标类
class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


 