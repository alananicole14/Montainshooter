#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass


#self.menu_text(text_size=50, text='Mountain', text_color=(255, 126, 0),
                           #text_center_pos=((WIN_WIDTH / 2), 70))
            #self.menu_text(text_size=50, text='Shooter', text_color=(255, 126, 0),
                           #text_center_pos=((WIN_WIDTH / 2), 120))
                           #            for i in range(len(MENU_OPTION)):
                #self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE,
                               #text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
