from Settings import *
from Textures import *


# Player Class
class Player(pygame.sprite.Sprite):
    jumpsLeft = 200
    yVel = 0
    xVel = 0
    maxVel = 60

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imgPLAYER)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        if self.yVel < self.maxVel:
            self.yVel += GRAVITY

        if self.rect.bottom + self.yVel > HEIGHT:
            self.yVel = 0
            self.rect.bottom = HEIGHT

        self.rect.x += self.xVel
        self.rect.y += self.yVel

    def control(self,control,modifier):
        if control == "SPACE" and modifier == 1 and self.jumpsLeft > 0:
            self.yVel = -JUMPHEIGHT
            self.jumpsLeft -= 1
        elif control == "D":
            self.xVel += RUNSPEED * modifier
        elif control == "A":
            self.xVel -= RUNSPEED * modifier
        elif control == "S" and modifier == 1:
            self.yVel = 1

    def collisionCheck(self,group):
        collisions = pygame.sprite.spritecollide(self,group,False)
        for objects in collisions:
            objects.collideWith(self)

