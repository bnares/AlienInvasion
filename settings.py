class Settings():

    def __init__(self):
        #initialize the game static settings
        self.screen_width = 600
        self.screen_height = 1200
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit =3

        #bullet settings

        self.bullet_speed =1.0
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3

        #alien settings

        self.alien_speed =1.0
        self.fleet_drop_speed =10

        # fleet direction of 1 represents right; -1 represents left

        self.fleet_direction = 1

        #how quickly the game speeds up

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """initialize the settings which change throught the game"""
        self.ship_speed =1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1


    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale




