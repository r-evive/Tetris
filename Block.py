from SingleBlock import *;
from Granica import *;
from Data import *;
from Ranking import *;
import random;
import pygame;
import time;

class Block(object):
    isDead = False;
    deadBlocks = list();
    heigh = 563;
    currentHeighCounter = 0;
    
    def __init__(self,mainScreen,imagesObject,ranking,nextBlocks,type, __blockPositionX, __blockPositionY):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__granica = Granica(7,49,self.__imagesObject.board_Image.get_size()[0],self.__imagesObject.board_Image.get_size()[1]);
        self.__ranking = ranking;
        self.type = type;
        self.__nextBlocks = nextBlocks;
        if(type == "I"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Red"),SingleBlock(__blockPositionX,__blockPositionY+27,"Red"),SingleBlock(__blockPositionX,__blockPositionY-27,"Red"),SingleBlock(__blockPositionX,__blockPositionY+54,"Red")];
        elif(type == "T"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX+27,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX-27,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX,__blockPositionY+27,"Yellow")];
        elif(type == "O"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Orange"),SingleBlock(__blockPositionX,__blockPositionY+27,"Orange"),SingleBlock(__blockPositionX-27,__blockPositionY,"Orange"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Orange")];
        elif(type == "L"):
            self.__body =[SingleBlock(__blockPositionX,__blockPositionY,"Green"),SingleBlock(__blockPositionX,__blockPositionY+27,"Green"),SingleBlock(__blockPositionX,__blockPositionY-27,"Green"),SingleBlock(__blockPositionX+27,__blockPositionY+27,"Green")];
        elif(type == "J"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Purple"),SingleBlock(__blockPositionX,__blockPositionY+27,"Purple"),SingleBlock(__blockPositionX,__blockPositionY-27,"Purple"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Purple")];
        elif(type == "S"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Blue"),SingleBlock(__blockPositionX+27,__blockPositionY,"Blue"),SingleBlock(__blockPositionX,__blockPositionY+27,"Blue"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Blue")];
        elif(type == "Z"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Pink"),SingleBlock(__blockPositionX-27,__blockPositionY,"Pink"),SingleBlock(__blockPositionX,__blockPositionY+27,"Pink"),SingleBlock(__blockPositionX+27,__blockPositionY+27,"Pink")];
    
    def __setList(self,type, __blockPositionX, __blockPositionY):
        self.type = type;
        if(type == "I"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Red"),SingleBlock(__blockPositionX,__blockPositionY+27,"Red"),SingleBlock(__blockPositionX,__blockPositionY-27,"Red"),SingleBlock(__blockPositionX,__blockPositionY+54,"Red")];
        elif(type == "T"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX+27,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX-27,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX,__blockPositionY+27,"Yellow")];
        elif(type == "O"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Orange"),SingleBlock(__blockPositionX,__blockPositionY+27,"Orange"),SingleBlock(__blockPositionX-27,__blockPositionY,"Orange"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Orange")];
        elif(type == "L"):
            self.__body =[SingleBlock(__blockPositionX,__blockPositionY,"Green"),SingleBlock(__blockPositionX,__blockPositionY+27,"Green"),SingleBlock(__blockPositionX,__blockPositionY-27,"Green"),SingleBlock(__blockPositionX+27,__blockPositionY+27,"Green")];
        elif(type == "J"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Purple"),SingleBlock(__blockPositionX,__blockPositionY+27,"Purple"),SingleBlock(__blockPositionX,__blockPositionY-27,"Purple"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Purple")];
        elif(type == "S"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Blue"),SingleBlock(__blockPositionX+27,__blockPositionY,"Blue"),SingleBlock(__blockPositionX,__blockPositionY+27,"Blue"),SingleBlock(__blockPositionX-27,__blockPositionY+27,"Blue")];
        elif(type == "Z"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Pink"),SingleBlock(__blockPositionX-27,__blockPositionY,"Pink"),SingleBlock(__blockPositionX,__blockPositionY+27,"Pink"),SingleBlock(__blockPositionX+27,__blockPositionY+27,"Pink")];
    
    def draw(self):
        for i in self.__body:
            if(i.positionY > self.__granica.Y):
                if(i.color == "Red"):
                    self.__mainScreen.blit(self.__imagesObject.redBlock_Texture,(i.positionX+1, i.positionY+1));
                elif(i.color == "Blue"):
                    self.__mainScreen.blit(self.__imagesObject.blueBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Orange"):
                    self.__mainScreen.blit(self.__imagesObject.orangeBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Purple"):
                    self.__mainScreen.blit(self.__imagesObject.purpleBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Green"):
                    self.__mainScreen.blit(self.__imagesObject.greenBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Pink"):
                    self.__mainScreen.blit(self.__imagesObject.pinkBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Yellow"):
                    self.__mainScreen.blit(self.__imagesObject.yellowBlock_Texture,(i.positionX, i.positionY));

        for i in self.deadBlocks:
            if(i.positionY > self.__granica.Y):
                if(i.color == "Red"):
                    self.__mainScreen.blit(self.__imagesObject.redBlock_Texture,(i.positionX+1, i.positionY+1));
                elif(i.color == "Blue"):
                    self.__mainScreen.blit(self.__imagesObject.blueBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Orange"):
                    self.__mainScreen.blit(self.__imagesObject.orangeBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Purple"):
                    self.__mainScreen.blit(self.__imagesObject.purpleBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Green"):
                    self.__mainScreen.blit(self.__imagesObject.greenBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Pink"):
                    self.__mainScreen.blit(self.__imagesObject.pinkBlock_Texture,(i.positionX, i.positionY));
                elif(i.color == "Yellow"):
                    self.__mainScreen.blit(self.__imagesObject.yellowBlock_Texture,(i.positionX, i.positionY));

    def __checkCollision(self, direction):
        if direction == "Left":
            for i in self.__body:
                if(i.positionX -27 < self.__granica.X):
                    return True;
        if direction == "Right":
            for i in self.__body:
                if(i.positionX +27 > self.__granica.Width):
                    return True;
        if direction == "Top":
            for i in self.__body:
                if(i.positionY -27< self.__granica.Y):
                    return True;
        if direction == "Bot":
            for i in self.__body:
                if(i.positionY > self.__granica.Height):
                    self.isDead = True;
                    return True;

        if direction == "ALL":
            for i in self.__body:
                if(i.positionX +20 < self.__granica.X):
                    return True;
                if(i.positionX > self.__granica.Width):
                    return True;
                if(i.positionY +20 < self.__granica.Y):
                    return True;
                if(i.positionY > self.__granica.Height):
                    return True;
        return False;

    def removeLayers(self):
            if(self.isDead == True):
                self.setToDeadBlocks();
            for t in range(0,20,1):
                for i in self.deadBlocks:
                    if(i.positionY == self.heigh - t*27):
                        self.currentHeighCounter = self.currentHeighCounter + 1;
                if(self.currentHeighCounter == 10):
                    e = 0;
                    Data.points += 2;
                    while(True):
                        if(e >= len(self.deadBlocks)):
                            break;
                        elif(self.deadBlocks[e].positionY == self.heigh-t*27):
                            del self.deadBlocks[e];
                            e = e - 1;
                        else:
                            e = e + 1;
                    for w in self.deadBlocks:
                        if(w.positionY <= self.heigh - t*27):
                            w.positionY = w.positionY + 27;
                    self.currentHeighCounter = 0;
                else:
                    self.currentHeighCounter = 0;


    def rotate(self):
        if(self.type !="O"):
            tempListaX = [0,0,0,0];
            tempListaY = [0,0,0,0];
            counter = 0;
            for r in self.__body:
                tempListaX[counter] = r.positionX;
                tempListaY[counter] = r.positionY;
                counter += 1;

            k = 0;
            for i in self.__body:
                if( k!= 0):
                    tempPosX = i.positionX;
                    tempPosY = i.positionY;
                    if((tempPosY > self.__body[0].positionY)):
                        i.positionY = i.positionY - (tempPosY - self.__body[0].positionY);
                        i.positionX = i.positionX - (tempPosY - self.__body[0].positionY);
                    elif((tempPosY < self.__body[0].positionY)):
                        i.positionY = i.positionY + (self.__body[0].positionY - tempPosY);
                        i.positionX = i.positionX - (tempPosY - self.__body[0].positionY);
                    if(tempPosX < self.__body[0].positionX):
                        i.positionY = i.positionY - (self.__body[0].positionX - tempPosX);
                        i.positionX = i.positionX - (tempPosX - self.__body[0].positionX);
                    elif(tempPosX > self.__body[0].positionX):
                        i.positionY = i.positionY + (tempPosX - self.__body[0].positionX);
                        i.positionX = i.positionX - (tempPosX - self.__body[0].positionX);

                    k += 1;
                else:
                    k += 1;

            secondCounter = 0;

            if(self.__checkCollision("ALL") == True or self.deadBlocksRotationCollisions() == True):
                for t in self.__body:
                    t.positionX = tempListaX[secondCounter];
                    t.positionY = tempListaY[secondCounter];
                    secondCounter +=1;
                    
    def __checkDeadBlockColisions(self,direction):
        for i in self.deadBlocks:
            for j in self.__body:
                if(direction == "Bot"):
                    if(j.positionX == i.positionX and j.positionY+27 == i.positionY):
                        self.isDead = True;
                        return True;
                elif(direction == "Left"):
                    if(j.positionX-27 == i.positionX and j.positionY == i.positionY):
                        return True;
                elif(direction == "Top"):
                    if(j.positionX == i.positionX and j.positionY-27 == i.positionY):
                        return True;
                elif(direction == "Right"):
                    if(j.positionX+27 == i.positionX and j.positionY == i.positionY):
                        return True;
        return False;

    def deadBlocksRotationCollisions(self):
            for i in self.deadBlocks:
                for j in self.__body:
                    if(i.positionX == j.positionX and i.positionY == j.positionY):
                        return True;
            return False;

    def getDeadBlocks(self,list):
        self.deadBlocks = list;

    def move(self,direction):
        xValue = 0;
        yValue = 0;
        if(direction == "Top" and self.__checkCollision("Top") == False and self.__checkDeadBlockColisions("Top") == False):
            yValue = -27;
        elif(direction == "Bot" and self.__checkCollision("Bot") == False and self.__checkDeadBlockColisions("Bot") == False):
            yValue += 27;
        elif(direction == "Left" and self.__checkCollision("Left") == False and self.__checkDeadBlockColisions("Left") == False):
            xValue = -27;
        elif(direction == "Right" and self.__checkCollision("Right") == False and self.__checkDeadBlockColisions("Right") == False):
            xValue = 27;
        for i in self.__body:
            i.positionX += xValue;
            i.positionY += yValue;
        self.removeLayers();

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

    def setControllerToDeafutPosition(self):
        self.__body.clear();
        self.__nextBlocks.getNewBlock();
        shape = self.__nextBlocks.currentBlock;
        if(shape == "O"):
            self.__setList(shape,61+54,-4);
        elif(shape == "I"):
            self.__setList(shape,61+54,-31);
        elif(shape == "T"):
            self.__setList(shape,61+54,-4);
        elif(shape == "S"):
            self.__setList(shape,61+54,-4);
        elif(shape == "Z"):
            self.__setList(shape,61+54,-4);
        elif(shape == "J"):
            self.__setList(shape,61+54,-4);
        elif(shape == "L"):
            self.__setList(shape,61+54,-4);

    def setToDeadBlocks(self):
        self.isDead = False;
        for i in self.__body:
            self.deadBlocks.append(i);
        for j in self.deadBlocks:
            if(j.positionY <=50):
                self.__ranking.saveCurrentStats();
                self.deadBlocks.clear();
                Data.points = 0;
                break;
        self.__body.clear();
        self.__nextBlocks.getNewBlock();
        shape = self.__nextBlocks.currentBlock;

        if(shape == "O"):
            self.__setList(shape,61+54,-4);
        elif(shape == "I"):
            self.__setList(shape,61+54,-31);
        elif(shape == "T"):
            self.__setList(shape,61+54,-4);
        elif(shape == "S"):
            self.__setList(shape,61+54,-4);
        elif(shape == "Z"):
            self.__setList(shape,61+54,-4);
        elif(shape == "J"):
            self.__setList(shape,61+54,-4);
        elif(shape == "L"):
            self.__setList(shape,61+54,-4);
