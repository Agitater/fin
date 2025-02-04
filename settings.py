import pygame as pg
# defining colours
white = (255, 255, 255)
black = (0, 0, 0)
grey = (40, 40, 40)
lgrey = (100, 100, 100)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# game settings
width = 1024
height = 768
fps = 100
title = "belly buddies"
backgroundcolour = grey

tilesize = 32
gridwidth = width / tilesize
gridheight = height / tilesize

# player settings
player_speed = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)