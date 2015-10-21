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


# x轴方向检测碰撞
def collision_x(co1, co2):
    if co2.x1 <= co1.x1 <= co2.x2:
        return True
    elif co2.x1 <= co1.x2 <= co2.x2:
        return True
    elif co1.x1 <= co2.x1 <= co1.x2:
        return True
    elif co1.x1 <= co2.x2 <= co1.x2:
        return True
    else:
        return False


def collision_y(co1, co2):
    if co2.y1 <= co1.y1 <= co2.y2:
        return True
    elif co2.y1 <= co1.y2 <= co2.y2:
        return True
    elif co1.y1 <= co2.y1 <= co1.y2:
        return True
    elif co1.y1 <= co2.y2 <= co1.y2:
        return True
    else:
        return False


def collision_left(colliding, collided):
    if collision_y(colliding, collided):
        if collided.x1 <= colliding.x1 <= collided.x2:
            return True
    return False


def collision_right(colliding, collided):
    if collision_y(colliding, collided):
        if collided.x1 <= colliding.x2 <= collided.x2:
            return True
    return False


def collision_bottom(colliding, collided, y=0):
    if collision_x(colliding, collided):
        y_calc = colliding.y2 + y
        if collided.y1 <= y_calc <= collided.y2:
            return True
    return False


def collision_top(colliding, collided):
    if collision_x(colliding, collided):
        if collided.y1 <= collided.y1 <= collided.y2:
            return True
    return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.end_game = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x+width, y+height)


g = Game()
platform1 = PlatformSprite(g, PhotoImage(file='plateformLong.gif'), 0, 480, 100, 10)
g.sprites.append(platform1)
g.mainloop()