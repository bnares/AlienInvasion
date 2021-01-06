import sys
import pygame
import settings
import ship
from bullet import Bullet
from alien import  Alien
from time import sleep
from game_stats import GameStats
from button import Button


class AlienInvasion():

    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Alien Invasion")

        # creating instance of GameStats class  to store statistics
        self.stats = GameStats(self)


        #number of lives
        self.ship = ship.Ship(self)

        #rysuj pelny ekran
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height


        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #Make the play button
        self.play_button = Button(self,"PLAY")






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
        if(len(self.bullets) < self.settings.bullet_allowed):
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def  _check_play_button(self, mouse_pos):
        """Start new game when a player click new game"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            #reset game statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            #get rid of any remaning aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)


    def _update_bullets(self):
        #Update bullets positions
        self.bullets.update()

        #get rid of of bullets that has dessepeard
        for bullet in self.bullets.copy():
            if(bullet.rect.bottom<0):
                self.bullets.remove(bullet)
        self._check_bullet_alien_colision()




    def _check_bullet_alien_colision(self):

        #respod to bullet alien colision
        # check for any bullets that have hit aliens
        # if so get rid of the bullet and ship

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True )

        if not self.aliens:
            #destroy exisisting bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        #update the positions of alien, check if the fleet is ath the edge. then update the posiotions of all aliens
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien-ship colision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens  hitting the bottom of the screen
        self._check_aliens_bottom()



    def _check_fleet_edges(self):
        """Respond approprietly if any aliens have reached edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1





    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Draw the play button
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()




    def run_game(self):

        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()

                #Get rid of the bullets that have dissepeard
                self._update_bullets()

                self._update_aliens()

            self._update_screen()



    def _create_fleet(self):
        """create the fleet of aliens"""
        '''spacing between each alien is equal to one alien'''

        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_height-(2*alien_width)
        number_of_aliens_x = available_space_x//(2*alien_width)

        # determine the number of rows of aliens that fit on the screen

        ship_height = self.ship.rect.height
        avilable_space_y = self.settings.screen_width-3*alien_height-ship_height
        number_rows = avilable_space_y // (2*alien_height)

        #create the full fleet of aleins

        for row_number in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number, row_number)



    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width+2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height+2*alien_height*row_number
        self.aliens.add(alien)


    def _ship_hit(self):
        """Respond to thee ship being hit by alien"""

        if self.stats.ships_left==0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        else:
            # decrement ships_left
            self.stats.ships_left -= 1

            # get rid of any remaning aliens
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)


    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break








ai = AlienInvasion()
ai.run_game()