import pygame

from screen import Screen
from map import Map
from keylistener import KeyListener

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen) #TODO créer une première map et la passer en parametre !!!
        self.keylistener = KeyListener()

    def run(self):
        while self.running:
            self.handle_input()
            #self.map.update() #TODO décommenter lorsque première map implémentée
            self.screen.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)