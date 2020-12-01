import pygame
import sys
from settings import Settings
from ship import Ship


class AlienInvasion():

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption(("ALIEN INVASION"))



    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.type == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.type == pygame.K_LEFT:
            self.ship.moving_left = False



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)






    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_Game(self):

        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()




if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_Game()

