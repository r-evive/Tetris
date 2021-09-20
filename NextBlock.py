from BlockPreview import *;
import random;

class NextBlock(object):

    def __init__(self,mainScreen,imagesObject,x,y):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__x = x;
        self.__y = y;
        self.__currentBlock = self.__getRandomShape();
        self.__firstBlock = BlockPreview(self.__mainScreen,self.__imagesObject,self.__getRandomShape(),self.__x+55,self.__y+70)
        self.__secondBlock = BlockPreview(self.__mainScreen,self.__imagesObject,self.__getRandomShape(),self.__x+55,self.__y+170)
        self.__thirdBlock = BlockPreview(self.__mainScreen,self.__imagesObject,self.__getRandomShape(),self.__x+55,self.__y+270);

    def draw(self):
        self.__mainScreen.blit(self.__imagesObject.nextBlocks_Image, (self.__x, self.__y));
        self.__firstBlock.draw();
        self.__secondBlock.draw();
        self.__thirdBlock.draw();

    def __getRandomShape(self):
        randomValue = random.randint(1,7);

        if(randomValue == 1):
            return "I";
        elif(randomValue == 2):
            return "O";
        elif(randomValue == 3):
            return "S";
        elif(randomValue == 4):
            return "Z";
        elif(randomValue == 5):
            return "J";
        elif(randomValue == 6):
            return "L";
        elif(randomValue == 7):
            return "T";

    def getNewBlock(self):
        self.__currentBlock = self.__firstBlock.type;
        self.__firstBlock = self.__secondBlock;
        self.__firstBlock.move(0,-100);
        self.__secondBlock = self.__thirdBlock;
        self.__secondBlock.move(0,-100);
        self.__thirdBlock = BlockPreview(self.__mainScreen,self.__imagesObject,self.__getRandomShape(),self.__x+55,self.__y+270);

    @property
    def currentBlock(self):
        return self.__currentBlock;