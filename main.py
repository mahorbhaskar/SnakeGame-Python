import pygame
import time
import random

pygame.init()

#define colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
orange=(255,165,0)

width,height=600,400

game_display=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
snake_size=10
snake_speed=15

message_font=pygame.font.SysFont('ubuntu',30)
score_font=pygame.font.SysFont('ubuntu',25)
