class Settings():

    def __init__(self):
        self.screen_width = 600
        self.screen_height = 1200
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5

        #bullet settings

        self.bullet_speed =1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #alien settings

        self.alien_speed =1.0
        self.fleet_drop_speed =10

        # fleet direction of 1 represents right; -1 represents left

        self.fleet_direction = 1



