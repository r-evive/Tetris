import pygame;
class Background(object):
    __x = 0;
    __mainMenuMoving = False;
    __logoMoveValue = 0;

    def __init__(self,screen,imagesObject):
        self.__mainScreen = screen;
        self.__imagesObject = imagesObject;

    def draw(self):
        moveValue = self.__x % 1974;
        self.__mainScreen.blit(self.__imagesObject.background_Image, (moveValue - 1974,0));
        if(moveValue < 1974):
            self.__mainScreen.blit(self.__imagesObject.background_Image,(moveValue,0));
        self.__x -= 0.15;

    def startMoving(self):
        self.__mainMenuMoving = True;

    def stopMoving(self, value):
        self.__mainMenuMoving = False;