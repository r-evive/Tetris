import pygame;
from Data import *;
class InputBox(object):

    __input = str();
    __inputWidth = 0;
    def __init__(self,screen,image,x1,y1):
        self.__mainScreen = screen;
        self.__image = image;
        self.__x1 = x1;
        self.__y1 = y1;
        self.__x2 = x1 + image.get_size()[0];
        self.__y2 = y1 + image.get_size()[1];
        self.__font = pygame.font.SysFont('arial',30);
       
    def draw(self):
        text = self.__font.render(self.__input, True, (0, 0, 0));
        self.__mainScreen.blit(self.__image,(self.__x1,self.__y1));
        self.__mainScreen.blit(text,(self.__x1 + self.__image.get_size()[0]/2 - self.__inputWidth ,self.__y1+60));

    def Handler(self,event): 
            if event.type == pygame.KEYDOWN:
                pygame.key.set_repeat(0,70);
                if(event.key >=97 and event.key <=122):
                    if(len(self.__input) < 11):
                        if(len(self.__input) == 0):
                            self.__input += chr(event.key).upper();
                        else:
                            self.__input += chr(event.key);
                        self.__inputWidth +=6;
                        Data.nickname = self.__input;
                elif(event.key == 8):
                    if(len(self.__input) != 0):
                        self.__input = self.__input[:len(self.__input)-1];
                        Data.nickname = self.__input;
                        self.__inputWidth -=6;
                elif(event.key == 13):
                    if(len(self.__input)>2):
                        Data.currentMode = "Menu";
                pygame.key.set_repeat(0,70);