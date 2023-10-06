import pygame
import sys
from const import *
from game import Game


class Main:
    def __init__(self):
        # Initializing pygame model
        pygame.init()
        # Creating a screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Setting a title
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        while True:
            game.show_bg(screen)
            for event in pygame.event.get():
                # Quit the game if the user clicks the X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update screen with any changes
            pygame.display.update()


main = Main()
main.mainloop()
