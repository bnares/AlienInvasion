import sys
import pygame
import settings
import ship
from bullet import Bullet


class AlienInvasion():

    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        self.ship = ship.Ship(self)

        #rysuj pelny ekran
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height


        self.bullets = pygame.sprite.Group()


    def _key_down(self, event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()


    def _key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _fire_bullet(self):
        """create new bullet and add it to he bullet group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event)


            elif event.type == pygame.KEYUP:
                self._key_up(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()



    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            #Get rid of the bullets that have dissepeard
            for bullet in self.bullets.copy():
                if(bullet.rect.bottom<=0):
                    self.bullets.remove(bullet)


            self._update_screen()




ai = AlienInvasion()
ai.run_game()