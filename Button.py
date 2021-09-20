import pygame;

class Button(object):
    __mouseAbove = False;

    def __init__(self,screen,imageOn,imageOff,x1,y1,method):
        self.__mainScreen = screen;
        self.__imageOn = imageOn;
        self.__imageOff = imageOff;
        self.__x1 = x1;
        self.__y1 = y1;
        self.__x2 = x1 + imageOff.get_size()[0];
        self.__y2 = y1 + imageOff.get_size()[1];
        self.__method = method;

    def draw(self):
        if(self.__mouseAbove == False):
            self.__mainScreen.blit(self.__imageOff,(self.__x1,self.__y1));
        else:
            self.__mainScreen.blit(self.__imageOn,(self.__x1,self.__y1));

    def Handler(self,event):
        position = pygame.mouse.get_pos();
        if(position[0]>=self.__x1 and position[0] <=self.__x2 and position[1] >= self.__y1 and position[1] <= self.__y2):
            self.__mouseAbove = True;
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(self.__method != None):
                    self.__method();
        else:
            self.__mouseAbove = False;

    def move(self,xValue, yValue):
        self.__x1 += xValue;
        self.__x2 += xValue;
        self.__y1 += yValue;
        self.__y2 += yValue;

    @property
    def mouseAbove(self):
        return self.__mouseAbove;
