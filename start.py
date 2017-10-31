#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame import *
import os

pygame.init(); 
pygame.font.init();
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096);

WIN_WIDTH = 800;
WIN_HEIGHT = 640;
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) ;
BACKGROUND_COLOR = "#004400";


directory = os.path.abspath(os.curdir);
files = os.listdir(directory);
(x, y, fontSize) = (10, 40, 50);
tFont = pygame.font.SysFont("None", fontSize)
fontColor = (255, 255, 0);
bgColor = (255, 255, 255);
startX = 100;
startY = 100;
space = 10;
time = 0;
m = pygame.mixer.music;
def main():
    screen = pygame.display.set_mode(DISPLAY); 
    pygame.display.set_caption("Bears");
    bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT));
    a = 1;
    c_x = 0;
    update = False;
    playing = False;
    c_y = 0;
    cube = pygame.Surface((fontSize - space, fontSize - space));
    cube.fill(pygame.Color("#250000"))
    bg.fill(pygame.Color(BACKGROUND_COLOR)) 
    def check(s, p):
    	if s[p] == 'g' and s[p-1] == 'g' and s[p-2] == 'o' and s[p-3] == ".":
    		print(".ogg")
    		return True;
    	if 	s[p] == '3' and s[p-1] == 'p' and s[p-2] == 'm' and s[p-3] == ".":
    		print(".mp3")
    		return True;
    def music(sound):
    	m.load(sound);
    	m.play(0, 0.0);
    	#else:	
		#	pass;

    			
    def go(i):
        update = False;
    	if i == "../":
    		os.chdir("../");
    		return 0;
    	elif os.path.isdir(files[i]):
    		os.chdir(files[i]);
    		return 0;
        elif os.path.isfile(files[i]) and check(files[i], len(files[i]) - 1):   
            music(files[i]);    
            return i;	
    def up():
    	text = tFont.render(directory.decode('utf-8'), 0, (fontColor));
        screen.blit(bg, (0,0));  
        screen.blit(text, (0,0));
        screen.blit(cube, (c_x, c_y));
        y = Y;
        for i in range(len(files)):
            if len(files) > 0:
                fi.append(tFont.render(files[i].decode('utf-8'), 0, (fontColor)));
                screen.blit(fi[i], (X, y)); 
                pygame.display.update(); 
                y += fontSize + space; 		
    while True:
    	tFont = pygame.font.SysFont("None", fontSize)
    	X = startX;
    	Y = startY;
    	directory = os.path.abspath(os.curdir);
    	files = os.listdir(directory);
    	#if len(directory) > 20: 
        #    fontSize = 25;
        #else:
        #    fontSize = 50;     
    	if a > len(files) - 1:
    		a = len(files) - 1;
    	elif a < 0:
    		a = 0;	
    	fi = [];
    	c_x = X - 50;
    	c_y = Y + (fontSize + space) * a;
    	if a > 5:
    		Y -= (fontSize + space) * (a - 5);
    		c_y -= (fontSize + space) * (a - 5);
    	if not update:
            up();
            update = True;
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                update = False;
            	if e.key == pygame.K_UP:
                    a -= 1;
            	if e.key == pygame.K_DOWN:
            		a += 1;
            	if e.key == pygame.K_RIGHT and len(files) > 0:
            		a = go(a);
            	if e.key == pygame.K_LEFT:
            		a = go("../");
            	if e.key == pygame.K_SPACE:
                    pass;		
            if e.type == QUIT:
                raise SystemExit("exit");

        pygame.display.update(); 
        if time != 0:
            pygame.time.wait(time)
        else:    
            pygame.time.wait(100)
        
        
if __name__ == "__main__":
    main();
