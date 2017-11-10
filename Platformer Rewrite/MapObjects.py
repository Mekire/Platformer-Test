from Settings import *
from Textures import *


# all objects on the map
class mapObject(pygame.sprite.Sprite):

    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)


# objects below inherit from mapObject
# platform object
class Platform(mapObject):
    texture = pygame.image.load(imgPLATFORM)

    def __init__(self,x,y):
        mapObject.__init__(self,x,y,self.texture)

    def collideWith(self):
        pass


# block object
class Block(mapObject):
    texture = pygame.image.load(imgBLOCK)

    def __init__(self,x,y):
        mapObject.__init__(self,x,y,self.texture)

    def collideWith(self,player):

        # collisions = []
        # collisions.append(player.rect.collidepoint(self.rect.topleft))
        # collisions.append(player.rect.collidepoint(self.rect.topright))
        # collisions.append(player.rect.collidepoint(self.rect.bottomleft))
        # collisions.append(player.rect.collidepoint(self.rect.bottomright))
        #
        # collisions.append(player.rect.collidepoint(self.rect.midleft))
        # collisions.append(player.rect.collidepoint(self.rect.midright))
        # collisions.append(player.rect.collidepoint(self.rect.midtop))
        # collisions.append(player.rect.collidepoint(self.rect.midbottom))
        #
        # print(collisions,"\n")


        #ISSUES:
        #High enough up/down velocity results in passing through blocks
        #Sideways collisions don't work at all

        if player.rect.top < self.rect.top:
            player.rect.bottom = self.rect.top
            player.yVel = 0
        if player.rect.bottom > self.rect.bottom:
            player.rect.top = self.rect.bottom
            player.yVel = 0



