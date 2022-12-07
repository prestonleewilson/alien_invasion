import pygame
import sys
from bulletclass import Bullet
pygame.init()
clock = pygame.time.Clock()
class all:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.instructions = pygame.image.load("images/instructions.bmp")
        self.bossinstructions = pygame.image.load("images/bossinstruct.bmp")
        self.image = pygame.image.load("images/cmod.bmp")
        self.image2 = pygame.image.load("images/cmod2.bmp")
        self.image3 = pygame.image.load("images/rat.bmp")
        self.image3a = pygame.image.load("images/rat.bmp")
        self.image3b = pygame.image.load("images/rat.bmp")
        self.image3c = pygame.image.load("images/rat.bmp")
        self.multi = pygame.image.load("images/ratking.bmp")
        self.image4 = pygame.image.load("images/fire.bmp")
        self.image4a = pygame.image.load("images/fire.bmp")
        self.image4b = pygame.image.load("images/fire.bmp")
        self.image4c = pygame.image.load("images/fire.bmp")
        self.image4d = pygame.image.load("images/fire.bmp")
        self.image5 = pygame.image.load("images/sir.bmp")
        self.image6 = pygame.image.load("images/sir.bmp")
        self.youlost = pygame.image.load("images/youlost.bmp")
        self.youwon = pygame.image.load("images/youwon.bmp")
        self.finalwin = pygame.image.load("images/finalwin.bmp")
        self.lock = pygame.image.load("images/lock.bmp")
        self.rifle = pygame.image.load("images/rifle.bmp")
        self.corepower = pygame.image.load("images/corepower.bmp")
        self.corepower_rect = self.corepower.get_rect()
        self.corepower_rect.x = 710
        self.corepower_rect.y = 627
        self.lock_rect = self.lock.get_rect()
        self.multi_rect = self.multi.get_rect()
        self.image5_rect = self.image5.get_rect()
        self.image6_rect = self.image6.get_rect()
        self.image3_rect = self.image3.get_rect()
        self.image3a_rect = self.image3a.get_rect()
        self.image3b_rect = self.image3b.get_rect()
        self.image3c_rect = self.image3c.get_rect()
        self.image4_rect = self.image4.get_rect
        self.image4a_rect = self.image4a.get_rect()
        self.image4b_rect = self.image4b.get_rect()
        self.image4c_rect = self.image4c.get_rect()
        self.image4d_rect = self.image4d.get_rect()
        self.image4_rect = self.image4.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.screen_rect.x = self.screen_rect.width
        self.screen_rect.y = self.screen_rect.height
        self.image_rect = self.image.get_rect()
        self.image_rect.y = 0
        self.image_rect.x = 0
        self.multi_rect.x = 1000
        self.multi_rect.y = 550
        self.multi_health = False
        self.yes = False
        self.win = False
        self.powerup = False
        self.finalscreen = False
        self.ratking_health = 2
        self.bulletnumber = 1
        self.locknum = 0
        self.move_down = False
        self.move_right = False
        self.move_up = False
        self.move_left = False
        self.move_r = False
        self.move_l = False
        self.move_u = False
        self.move_d = False
        self.shoot = False
        self.checkrifle = False
        self.check = 0
        self.instructboss = False
        self.tile = pygame.image.load("images/tile.bmp")
        self.tile_rect = self.tile.get_rect()
        self.tile_rect.y = self.tile_rect.height
        self.tile_rect.x = self.tile_rect.width
        self.plate = pygame.image.load("images/plate.bmp")
        self.plate_rect = self.plate.get_rect()
        self.plate_rect.y = self.plate_rect.height
        self.plate_rect.x = self.plate_rect.width
        self.cheese = pygame.image.load("images/cheese.bmp")
        self.cheese_rect = self.cheese.get_rect()
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.bullets = pygame.sprite.Group()
        self.speed = 2
        self.rat = True
        self.rata = True
        self.ratc = False
        self.ratb = False
        self.fire = True
        self.firea = True
        self.fireb = False
        self.firec = False
        self.fired = False
        self.sir = True
        self.maam = True
        self.instruct = True
        self.block1 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 0, 700, 100))
        self.block1port = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 0, 700, 1))
        self.blocka = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 0, 1, 100))
        self.blocka1 = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(101, 0, 1, 98))
        self.blockb = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 100, 500, 1))
        self.blockbone = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(101, 99, 500, 1))
        self.blockb1 = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(680, 100, 120, 1))
        self.blockb1a = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(680, 99, 120, 1))
        self.door = pygame.draw.rect(self.screen, (200, 80, 0), pygame.Rect(600, 96, 80, 4))
        self.blockc = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(800, 0, 1, 100))
        self.blockc1 = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(799, 0, 1, 99))
        self.block2 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 0, 400, 100))
        self.blockd = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 0, 4, 100))
        self.blocke = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 99, 1300, 4))
        self.block3 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 200, 700, 200))
        self.blockf = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 200, 4, 200))
        self.blockg = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 200, 700, 4))
        self.blockh = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(800, 200, 4, 200))
        self.blocki = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 400, 700, 4))
        self.block4 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 200, 400, 200))
        self.blockj = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 200, 4, 200))
        self.blockk = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 200, 400, 4))
        self.blockl = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 400, 400, 4))
        self.block5 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 500, 700, 220))
        self.blockm = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 500, 4, 220))
        self.blockn = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(100, 500, 700, 4))
        self.blocko = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(800, 500, 4, 220))
        self.block6 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 500, 400, 220))
        self.blockp = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 500, 4, 220))
        self.blockq = pygame.draw.rect(self.screen, (30, 80, 200), pygame.Rect(900, 500, 400, 4))
    def draw_background(self):
        # tiles my bancroft tiles in a hallway
        for i in range(0, 40):
            for a in range(0, 5):
                self.screen.blit(self.tile, (self.tile_rect.x*a, self.tile_rect.y*i))
        for i in range(20, 25):
            for a in range(0, 65):
                self.screen.blit(self.tile, (self.tile_rect.x*a, self.tile_rect.y*i))
        for i in range(0, 40):
            for a in range(40, 45):
                self.screen.blit(self.tile, (self.tile_rect.x*a, self.tile_rect.y*i))
        for i in range(5, 10):
            for a in range(0, 65):
                self.screen.blit(self.tile, (self.tile_rect.x*a, self.tile_rect.y*i))

        # places deck plates
        self.screen.blit(self.plate, (40, 440))
        self.screen.blit(self.plate, (40, 140))
        self.screen.blit(self.plate, (40, 640))
        self.screen.blit(self.plate, (840, 140))
        self.screen.blit(self.plate, (840, 440))
        self.screen.blit(self.plate, (840, 640))
        self.screen.blit(self.plate, (400, 140))
        self.screen.blit(self.plate, (1200, 140))
        self.screen.blit(self.plate, (400, 440))
        self.screen.blit(self.plate, (1200, 440))


        # draws each rectangle on either side of hallway(check for collisions with each rect)
        self.block1 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 0, 700, 100))
        self.block1port = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 0, 700, 1))
        self.blocka = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(100, 0, 1, 100))
        self.blocka1 = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 0, 1, 98))
        self.blockb = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 100, 500, 1))
        self.blockbone = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 99, 498, 1))
        self.blockb1 = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(680, 100, 120, 1))
        self.blockb1a = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(680, 99, 120, 1))
        self.door = pygame.draw.rect(self.screen, (200, 80, 0), pygame.Rect(600, 96, 80, 4))
        self.blockc = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(800, 0, 1, 100))
        self.blockc1 = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(799, 0, 1, 99))
        self.block2 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 0, 400, 100))
        self.blockd = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(900, 0, 4, 100))
        self.blocke = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(902, 99, 320, 4))
        self.blockesecret = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(1222, 99, 80, 4))
        self.block3 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 200, 700, 200))
        self.blockf = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(100, 202, 4, 198))
        self.blockg = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 200, 698, 4))
        self.blockh = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(800, 202, 4, 197))
        self.blocki = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 400, 698, 4))
        self.block4 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 200, 400, 200))
        self.blockj = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(900, 203, 4, 197))
        self.blockk = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(903, 200, 397, 4))
        self.blockl = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(903, 400, 398, 4))
        self.block5 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(100, 500, 700, 220))
        self.blockm = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(100, 600, 2, 118))
        self.blockma = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(102, 600, 2, 118))
        self.blockmb = pygame.draw.rect(self.screen, (200, 80, 0), pygame.Rect(102, 502, 4, 97 ))
        self.blockn = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(104, 500, 696, 2))
        self.blockna = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(104, 502, 696, 2))
        self.blockbuffer = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(100, 500, 4, 4))
        self.blocko = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(800, 502, 2, 220))
        self.blockoa = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(798, 502, 2, 218))
        self.block6 = pygame.draw.rect(self.screen, (60, 60, 60), pygame.Rect(900, 500, 400, 220))
        self.blockp = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(900, 502, 4, 218))
        self.blockq = pygame.draw.rect(self.screen, (130, 80, 200), pygame.Rect(902, 502, 398, 4))
    def check_events(self):
        # checks for keydown and keyup and sets things in motion based on true or false
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.yes = True
                if event.key == pygame.K_DOWN:
                    self.move_down = True
                if event.key == pygame.K_s:
                    self.move_d = True
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                if event.key == pygame.K_w:
                    self.move_u = True
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                if event.key == pygame.K_a:
                    self.move_l = True
                if event.key == pygame.K_UP:
                    self.move_up = True
                if event.key == pygame.K_d:
                    self.move_r = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
                if event.key == pygame.K_RETURN:
                    self.instruct = False
                if event.key == pygame.K_b:
                    self.win = False
                    self.instructboss = True
                if event.key == pygame.K_c:
                    self.instructboss = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.move_d = False
                if event.key == pygame.K_w:
                    self.move_u = False
                if event.key == pygame.K_a:
                    self.move_l = False
                if event.key == pygame.K_d:
                    self.move_r = False
                if event.key == pygame.K_DOWN:
                    self.move_down = False
                if event.key == pygame.K_RIGHT:
                    self.move_right = False
                if event.key == pygame.K_UP:
                    self.move_up = False
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                if event.key == pygame.K_m:
                    self.yes = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()

        # keeps image on screen or teleports them onto the other side
        if self.image_rect.right  >= self.screen_rect.x:
            self.image_rect.x = 0
            self.image_rect.y = self.image_rect.y
        if self.image_rect.left  <= 0:
            self.move_left = False
        if self.image_rect.bottom  >= self.screen_rect.y:
            self.image_rect.x = self.image_rect.x
            self.image_rect.y = 0
        if self.image_rect.top  < 0:
            self.image_rect.x = self.image_rect.x
            self.image_rect.y = 650

        if self.multi_rect.right  >= self.screen_rect.x:
            self.move_r = False
        if self.multi_rect.left  <= 0:
            self.move_l = False
        if self.multi_rect.bottom  >= self.screen_rect.y:
            self.move_d = False
        if self.multi_rect.top  < 0:
            self.move_u = False



        self.rect.x = self.image_rect.x
        self.rect.y = self.image_rect.y
    def _fire_bullet(self):
        if len(self.bullets) < self.bulletnumber:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right > 1300:
                self.bullets.remove(bullet)

    def update(self):
        self.draw_background()
        # check for condition to see if image can move
        if self.image_rect.colliderect(self.blocka):
            self.move_right = False
        if self.image_rect.colliderect(self.block1port):
            self.move_up = False
        if self.image_rect.colliderect(self.blocka1):
            self.move_left = False
        if self.image_rect.colliderect(self.blockb):
            self.move_up = False
        if self.image_rect.colliderect(self.door):
            self.move_right = False
            self.move_left = False
        if self.image_rect.colliderect(self.blockbone):
            self.move_down = False
        if self.image_rect.colliderect(self.blockb1):
            self.move_up = False
        if self.image_rect.colliderect(self.blockb1a):
            self.move_down = False
        if self.image_rect.colliderect(self.blockc):
            self.move_left = False
        if self.image_rect.colliderect(self.blockc1):
            self.move_right = False
        if self.image_rect.colliderect(self.blockd):
            self.move_right = False
        if self.image_rect.colliderect(self.blocke):
            self.move_up = False
        if self.image_rect.colliderect(self.blockf):
            self.move_right = False
        if self.image_rect.colliderect(self.blockg):
            self.move_down = False
        if self.image_rect.colliderect(self.blockh):
            self.move_left = False
        if self.image_rect.colliderect(self.blocki):
            self.move_up = False
        if self.image_rect.colliderect(self.blockj):
            self.move_right = False
        if self.image_rect.colliderect(self.blockk):
            self.move_down = False
        if self.image_rect.colliderect(self.blockl):
            self.move_up = False
        if self.image_rect.colliderect(self.blockm):
            self.move_right = False
        if self.image_rect.colliderect(self.blockma):
            self.move_left = False
        if self.image_rect.colliderect(self.blockmb):
            self.move_down = False
        if self.image_rect.colliderect(self.blockn):
            self.move_down = False
        if self.image_rect.colliderect(self.blockna):
            self.move_up = False
        if self.image_rect.colliderect(self.blockbuffer):
            self.move_right = False
        if self.image_rect.colliderect(self.blocko):
            self.move_left = False
        if self.image_rect.colliderect(self.blockoa):
            self.move_right = False
        if self.image_rect.colliderect(self.blockp):
            self.move_right = False
        if self.image_rect.colliderect(self.blockq):
            self.move_down = False
        # sets in motion enemy rat
        if self.rat == True:
            if self.image3_rect.x > 0:
                self.image3_rect.x -= 2
            if self.image3_rect.x <= 0:
                self.image3_rect.x = 1350
            self.screen.blit(self.image3, (self.image3_rect.x, 470))
        if self.rat == False:
            self.image3_rect.x = 1600

        if self.rata == True:
            if self.image3a_rect.x > 0:
                self.image3a_rect.x -= 2
            if self.image3a_rect.x <= 0:
                self.image3a_rect.x = 1350
            self.screen.blit(self.image3a, (self.image3a_rect.x, 175))
        if self.rata == False:
            self.image3a_rect.x = 1600

        if self.ratc == True:
            if self.image3c_rect.x > 0:
                self.image3c_rect.x -= 2
            if self.image3c_rect.x <= 0:
                self.image3c_rect.x = 1350
            self.screen.blit(self.image3c, (self.image3c_rect.x, 175))
        if self.ratc == False:
            self.image3c_rect.x = 1600

        if self.ratb == True:
            if self.image3b_rect.y > 0:
                self.image3b_rect.y += 2
            if self.image3b_rect.y >= 805:
                self.image3b_rect.y = 5
            self.screen.blit(self.image3b, (870, self.image3b_rect.y))
        if self.ratb == False:
            self.image3b_rect.y = 1600

        # sets in motion enemy fire
        if self.fire == True:
            if self.image4_rect.x > 0:
                self.image4_rect.x -= 1
            if self.image4_rect.x  <= 0:
                self.image4_rect.x = 1350
            self.screen.blit(self.image4, (self.image4_rect.x, 103))
        if self.fire == False:
            self.image4_rect.x = 1600

        if self.firea == True:
            if self.image4a_rect.x > 0:
                self.image4a_rect.x -= 1
            if self.image4a_rect.x  <= 0:
                self.image4a_rect.x = 1350
            self.screen.blit(self.image4a, (self.image4a_rect.x, 403))
        if self.firea == False:
            self.image4a_rect.x = 1600

        if self.fireb == True:
            if self.image4b_rect.y > 0:
                self.image4b_rect.y += 2
            if self.image4b_rect.y  >= 805:
                self.image4b_rect.y = 5
            self.screen.blit(self.image4b, (5, self.image4b_rect.y))
        if self.fireb == False:
            self.image4b_rect.y = 1000

        if self.firec == True:
            if self.image4c_rect.y > 0:
                self.image4c_rect.y -= 2
            if self.image4c_rect.y  <= 0:
                self.image4c_rect.y = 805
            self.screen.blit(self.image4c, (60, self.image4c_rect.y))
        if self.firec == False:
            self.image4c_rect.y = 1000

        if self.fired == True:
            if self.image4d_rect.y > 0:
                self.image4d_rect.y += 2
            if self.image4d_rect.y >= 805:
                self.image4d_rect.y = 5
            self.screen.blit(self.image4d, (870, self.image4d_rect.y))
        if self.fired == False:
            self.image4d_rect.y = 1600

        if self.sir == True:
            if self.image5_rect.y > 0:
                self.image5_rect.y -= 1
            if self.image5_rect.y <= 0:
                self.image5_rect.y = 700
            self.screen.blit(self.image5, (805, self.image5_rect.y))
        if self.sir == False:
            self.image5_rect.y = 1600

        # sets officer in motion
        if self.maam == True:
            if self.image6_rect.y < 805:
                self.image6_rect.y += 1
            if self.image6_rect.y >= 795:
                self.image6_rect.y = 0
            self.screen.blit(self.image6, (50, self.image6_rect.y))
        if self.maam == False:
            self.image6_rect.y = 1600
        # moves image based off key press
        if self.move_down == True:
            self.image_rect.y += 2
        if self.move_right == True:
            self.image_rect.x += 2
        if self.move_up == True:
            self.image_rect.y -= 2
        if self.move_left == True:
            self.image_rect.x -= 2
        self.screen.blit(self.image, (self.image_rect.x, self.image_rect.y))

        # moves multiplayer wasd keys
        if self.move_d == True:
            self.multi_rect.y += 2
        if self.move_r == True:
            self.multi_rect.x += 2
        if self.move_u == True:
            self.multi_rect.y -= 2
        if self.move_l == True:
            self.multi_rect.x -= 2
        if self.multi_health == True:
            self.screen.blit(self.multi, (self.multi_rect.x, self.multi_rect.y))

        if self.yes == True:
            self.screen.blit(self.image2, (self.image_rect.x, self.image_rect.y))
        # draws each bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # powerups!!
        if self.image_rect.colliderect(self.corepower_rect.x, 627, 36, 90) and self.check == 1 and self.powerup == True:
            self.image = pygame.image.load("images/cmod.bmp")
            self.check = 0
            self.powerup = False

        if self.image_rect.colliderect(self.corepower_rect.x, 627, 36, 90) and self.check == 0 and self.powerup == True:
            self.image = pygame.image.load("images/cmod.bmp")
            self.check = 0
            self.powerup = False

        if self.image_rect.colliderect(self.corepower_rect.x, 627, 36, 90) and self.check == 2 and self.powerup == True:
            self.image = pygame.image.load("images/cmod.bmp")
            self.check = 0
            self.powerup = False

        #Josh Doughty helped me with sound for collisions.
        # check for collision then plays sound based on colision
        # set up a system to track lives left and change image based on damage taken
        if self.image_rect.colliderect(self.image3_rect.x, 470, 30, 24) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image3_rect.x = 1350
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3_rect.x, 470, 30, 24) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image3_rect.x = 1350
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3_rect.x, 470, 30, 24) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()

        if self.image_rect.colliderect(self.image3a_rect.x, 175, 30, 24) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image3a_rect.x = 1350
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3a_rect.x, 175, 30, 24) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image3a_rect.x = 1350
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3a_rect.x, 175, 30, 24) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()

        if self.image_rect.colliderect(self.image3c_rect.x, 175, 30, 24) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image3c_rect.x = 1350
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3c_rect.x, 175, 30, 24) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image3c_rect.x = 1350
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image3c_rect.x, 175, 30, 24) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()

        if self.image_rect.colliderect(870, self.image3b_rect.y, 30, 24) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image3b_rect.y = 806
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(870, self.image3b_rect.y, 30, 24) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image3b_rect.y = 806
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(870, self.image3b_rect.y, 30, 24) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.image3b_rect.y = 806
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()

        if self.image_rect.colliderect(870, self.image4d_rect.y, 30, 52) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image4d_rect.y = 806
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(870, self.image4d_rect.y, 30, 52) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image4d_rect.y = 806
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(870, self.image4d_rect.y, 30, 52) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.image4d_rect.y = 806
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()

        if self.image_rect.colliderect(self.image4_rect.x, 103, 30, 52) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image4_rect.x = 1350
            self.check = 1
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image4_rect.x, 103, 30, 52) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image4_rect.x = 1350
            self.check = 2
            pygame.mixer.Sound("boom.mp3").play()
        if self.image_rect.colliderect(self.image4_rect.x, 103, 30, 52) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3
            pygame.mixer.Sound("boom.mp3").play()
        if self.check == 3:
            self.screen.blit(self.youlost, (0, 0))

        if self.image_rect.colliderect(self.image4a_rect.x, 403, 30, 52) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image4a_rect.x = 1350
            self.check = 1
        if self.image_rect.colliderect(self.image4a_rect.x, 403, 30, 52) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image4a_rect.x = 1350
            self.check = 2
        if self.image_rect.colliderect(self.image4a_rect.x, 403, 30, 52) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3

        if self.image_rect.colliderect(5, self.image4b_rect.y, 30, 52) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image4b_rect.y = 806
            self.check = 1
        if self.image_rect.colliderect(5, self.image4b_rect.y, 30, 52) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image4b_rect.y = 806
            self.check = 2
        if self.image_rect.colliderect(5, self.image4b_rect.y, 30, 52) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.image4b_rect.y = 806
            self.check = 3

        if self.image_rect.colliderect(805, self.image5_rect.y, 40, 40) and self.yes == True:
            self.sir = False

        if self.image_rect.colliderect(50, self.image6_rect.y, 40, 40) and self.yes == True:
            self.maam = False

        if self.image_rect.colliderect(60, self.image4c_rect.y, 30, 52) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.image4c_rect.y = 806
            self.check = 1
        if self.image_rect.colliderect(60, self.image4c_rect.y, 30, 52) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.image4c_rect.y = 806
            self.check = 2
        if self.image_rect.colliderect(60, self.image4c_rect.y, 30, 52) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.check = 3

        if self.image_rect.colliderect(self.multi_rect.x, self.multi_rect.y, 50, 40) and self.check == 0:
            self.image = pygame.image.load("images/cmod1st.bmp")
            self.multi_rect.y = 550
            self.multi_rect.x = 1000
            self.check = 1
        if self.image_rect.colliderect(self.multi_rect.x, self.multi_rect.y, 50, 40) and self.check == 1:
            self.image = pygame.image.load("images/cmod2nd.bmp")
            self.multi_rect.y = 550
            self.multi_rect.x = 1000
            self.check = 2
        if self.image_rect.colliderect(self.multi_rect.x, self.multi_rect.y, 50, 40) and self.check == 2:
            self.image = pygame.image.load("images/cmod3rd.bmp")
            self.multi_rect.y = 550
            self.multi_rect.x = 1000
            self.check = 3

        # check for collisions with bullets
        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.multi_rect.x, self.multi_rect.y, 50, 40) and self.ratking_health == 2:
                self.bullets.remove(bullet)
                self.multi_rect.x = 1000
                self.multi_rect.y = 350
                self.ratking_health = 1


            if self.bulletnumber == 10:
                if bullet.rect.colliderect(self.multi_rect.x, self.multi_rect.y, 50, 40) and self.ratking_health == 1:
                    self.bullets.remove(bullet)
                    self.multi_health = False
                    self.finalscreen = True
            if bullet.rect.colliderect(self.image3_rect.x, 470, 30, 24):
                self.bullets.remove(bullet)
                self.rat = False
                self.fireb = True
                self.ratb = True
                self.powerup = True
            if bullet.rect.colliderect(self.image3a_rect.x, 175, 30, 24):
                self.bullets.remove(bullet)
                self.rata = False
                self.firec = True
            if bullet.rect.colliderect(870, self.image3b_rect.y, 30, 24):
                self.bullets.remove(bullet)
                self.ratb = False
                self.ratc = True
                self.fired = True

            if bullet.rect.colliderect(self.image3c_rect.x, 175, 30, 24):
                self.bullets.remove(bullet)
                self.ratc = False
                self.locknum = 1

        if self.locknum == 1 and self.sir == False and self.maam == False:
            self.screen.blit(self.lock,(220, 25))
            if self.image_rect.colliderect(220, 25, 70, 70):
                self.checkrifle = True

        if self.checkrifle == True:
            self.screen.blit(self.rifle, (300, 600))
            if self.image_rect.colliderect(300, 600, 110, 61):
                self.win = True

        if self.image_rect.colliderect(904, 506, 10, 10):
            self.win = True

        if self.win == True:
            self.screen.blit(self.youwon, (0, 0))
            self.image_rect.x = 0
            self.image_rect.y = 0
            self.fire = False
            self.firea = False
            self.fireb = False
            self.firec = False
            self.fired = False
            self.multi_health = True
            self.bulletnumber = 10
            self.check = 0
            self.image = pygame.image.load("images/cmod.bmp")
            self.checkrifle = False
            self.locknum = 0
            self.powerup = False
        if self.instruct == True:
            self.screen.blit(self.instructions, (0, 0))
            self.move_up = False
            self.move_down = False
            self.move_right = False
            self.move_left = False
        if self.instructboss == True:
            self.screen.blit(self.bossinstructions, (0,0))
        if self.finalscreen == True:
            self.screen.blit(self.finalwin, (0, 0))


        if self.powerup == True:
            self.screen.blit(self.corepower, (710, 627))
        pygame.display.flip()

instance = all()
while True:
    instance.check_events()
    instance.update_bullets()
    instance.update()
    clock.tick(200)


