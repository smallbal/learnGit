# !/usr/bin/env python3
# -*-coding=utf-8-*-

from tkinter import *
# import random
import time


class Platform(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()


class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.hit_bottom = False
        self.x_pixel_of_one_step = 0  # 小球横向速度
        self.y_pixel_of_one_step = 3  # 小球纵向速度

    def hit_paddle(self, position):
        pass

    def draw(self):
        ball_pos = self.canvas.coords(self.id)
        paddle_pos = paddle.canvas.coords(paddle.id)
        if ball_pos[1] <= 0 or ball_pos[3] >= 500:
            self.y_pixel_of_one_step = 0 - self.y_pixel_of_one_step
        self.canvas.move(self.id, self.x_pixel_of_one_step, self.y_pixel_of_one_step)
        '''
        if ball_pos[3]>=paddle_pos[1] and self.y_pixel_of_one_step>0:
            if ball_pos[0]>=paddle_pos[0] and ball_pos[2]<=paddle_pos[2]:
                self.y_pixel_of_one_step = 0 - self.y_pixel_of_one_step
                self.canvas.move(self.id, self.x_pixel_of_one_step,self.y_pixel_of_one_step)
                return
        if ball_pos[1]<=paddle_pos[3] and self.y_pixel_of_one_step<0:
            if ball_pos[0]>=paddle_pos[0] and ball_pos[2]<=paddle_pos[2]:
                self.y_pixel_of_one_step = 0 - self.y_pixel_of_one_step
        self.canvas.move(self.id, self.x_pixel_of_one_step, self.y_pixel_of_one_step)
        '''


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 250, 250)
        self.canvas.bind_all('<KeyPress-Right>', self.move2right)
        self.canvas.bind_all('<KeyPress-Left>', self.move2left)
        self.x_pixel_of_one_step = 0
        self.y_pixel_of_one_step = 0

    def move2left(self, event):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x_pixel_of_one_step = 0
        else:
            self.x_pixel_of_one_step = -5
        self.canvas.move(self.id, self.x_pixel_of_one_step, self.y_pixel_of_one_step)

    def move2right(self, event):
        pos = self.canvas.coords(self.id)
        if pos[2] >= 500:
            self.x_pixel_of_one_step = 0
        else:
            self.x_pixel_of_one_step = 5
        self.canvas.move(self.id, self.x_pixel_of_one_step, self.y_pixel_of_one_step)

    def draw(self):
        pass


tk = Tk()
tk.title('Fuck The Ping-Pang')
tk.resizable(0, 0)  # 限制画布不能伸缩
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk,width=500, height=500, bd=0, highlightthickness=0)
# canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'black')
ball = Ball(canvas, 'black', paddle)

# tk.mainloop()
while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)