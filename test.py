# !/usr/bin/env python3
# coding=utf-8

from tkinter import *
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.hit_bottom = False
        self.x_pixel_of_one_step = 0  # 小球横向速度
        self.y_pixel_of_one_step = -3  # 小球纵向速度

    def draw(self):
        position = self.canvas.coords(self.id)
        if position[1]<=0 or position[3]>=500:
            self.y_pixel_of_one_step = 0-self.y_pixel_of_one_step
        self.canvas.move(self.id, self.x_pixel_of_one_step, self.y_pixel_of_one_step)


tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()
ball1 = Ball(canvas, 'black')
ball2 = Ball(canvas, 'red')
ball2.canvas.move(ball2.id, 100, 0)
while True:
    ball1.draw()
    ball2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)