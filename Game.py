from Board import *;
from Data import *;
from Block import *;
from NextBlock import *;
from Ranking import *;
import pygame;

class Game(object):
    __counter = 0;

    def __init__(self,mainScreen,imagesObject,ranking,x,y):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__x = x;
        self.__y = y;
        self.__ranking = ranking;
        self.__board = Board(self.__mainScreen,self.__imagesObject,self.__x + 7, self.__y + 49);
        self.__nextBlocks = NextBlock(self.__mainScreen,self.__imagesObject,self.__x + 295, self.__y + 200);
        self.__block = Block(self.__mainScreen,self.__imagesObject,self.__ranking,self.__nextBlocks,"O",self.__x + 61+54, self.__y - 4);
        self.__font = pygame.font.SysFont('arial',30);

    def draw(self):
        if(Data.currentMode == "Game"):
            self.__mainScreen.blit(self.__imagesObject.boardBackground, (self.__x + 7, self.__y + 49));
            self.__nextBlocks.draw();
            self.__block.draw();
            self.__board.draw();
            self.__mainScreen.blit(self.__imagesObject.points_Image, (self.__x + 295, self.__y + 110));
            text = self.__font.render(str(Data.points), True, (255, 255, 255));
            self.__mainScreen.blit(text,(self.__x + self.__imagesObject.points_Image.get_size()[0]/2+288 - self.__getMoveValue()*6 ,self.__y+141));

            if(self.__counter == 40):
                self.__block.move("Bot");
                self.__counter = 0;
            self.__counter += 1;
        elif(Data.currentMode == "Menu"):
            self.__block.deadBlocks.clear();
            self.__block.setControllerToDeafutPosition();
            Data.points = 0;

    def Handler(self,event):
        if(Data.currentMode == "Game"):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.__ranking.readStats();
                    self.__block.move("Bot");
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.__block.move("Left");
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.__block.move("Right");
                elif event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(0,32);
                    self.__block.rotate();
                    pygame.key.set_repeat(70,32);

       

    def wypisz(self):
        print("Wypisz");
    def __getMoveValue(self):
        i = Data.points;
        counter = 0;
        while i >= 10:
            i = i / 10;
            counter += 1;
        return counter;