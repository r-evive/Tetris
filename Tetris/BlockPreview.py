from SingleBlock import *;

class BlockPreview(object):

    def __init__(self,mainScreen,imagesObject,type, __blockPositionX, __blockPositionY):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;

        self.type = type;
        if(type == "I"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Red"),SingleBlock(__blockPositionX,__blockPositionY+20,"Red"),SingleBlock(__blockPositionX,__blockPositionY-20,"Red"),SingleBlock(__blockPositionX,__blockPositionY+40,"Red")];
        elif(type == "T"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX+20,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX-20,__blockPositionY,"Yellow"),SingleBlock(__blockPositionX,__blockPositionY+20,"Yellow")];
        elif(type == "O"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Orange"),SingleBlock(__blockPositionX,__blockPositionY+20,"Orange"),SingleBlock(__blockPositionX-20,__blockPositionY,"Orange"),SingleBlock(__blockPositionX-20,__blockPositionY+20,"Orange")];
        elif(type == "L"):
            self.__body =[SingleBlock(__blockPositionX,__blockPositionY,"Green"),SingleBlock(__blockPositionX,__blockPositionY+20,"Green"),SingleBlock(__blockPositionX,__blockPositionY-20,"Green"),SingleBlock(__blockPositionX+20,__blockPositionY+20,"Green")];
        elif(type == "J"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Purple"),SingleBlock(__blockPositionX,__blockPositionY+20,"Purple"),SingleBlock(__blockPositionX,__blockPositionY-20,"Purple"),SingleBlock(__blockPositionX-20,__blockPositionY+20,"Purple")];
        elif(type == "S"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Blue"),SingleBlock(__blockPositionX+20,__blockPositionY,"Blue"),SingleBlock(__blockPositionX,__blockPositionY+20,"Blue"),SingleBlock(__blockPositionX-20,__blockPositionY+20,"Blue")];
        elif(type == "Z"):
            self.__body = [SingleBlock(__blockPositionX,__blockPositionY,"Pink"),SingleBlock(__blockPositionX-20,__blockPositionY,"Pink"),SingleBlock(__blockPositionX,__blockPositionY+20,"Pink"),SingleBlock(__blockPositionX+20,__blockPositionY+20,"Pink")];
    
    def draw(self):
        for i in self.__body:
            if(i.color == "Red"):
                self.__mainScreen.blit(self.__imagesObject.redBlockPreview_Texture,(i.positionX, i.positionY));
            elif(i.color == "Blue"):
                self.__mainScreen.blit(self.__imagesObject.blueBlockPreview_Texture,(i.positionX, i.positionY));
            elif(i.color == "Orange"):
                self.__mainScreen.blit(self.__imagesObject.orangeBlockPreview_Texture,(i.positionX+10, i.positionY));
            elif(i.color == "Purple"):
                self.__mainScreen.blit(self.__imagesObject.purpleBlockPreview_Texture,(i.positionX, i.positionY));
            elif(i.color == "Green"):
                self.__mainScreen.blit(self.__imagesObject.greenBlockPreview_Texture,(i.positionX, i.positionY));
            elif(i.color == "Pink"):
                self.__mainScreen.blit(self.__imagesObject.pinkBlockPreview_Texture,(i.positionX, i.positionY));
            elif(i.color == "Yellow"):
                self.__mainScreen.blit(self.__imagesObject.yellowBlockPreview_Texture,(i.positionX, i.positionY));

    def move(self, valueX, valueY):
        for i in self.__body:
            i.positionX += valueX;
            i.positionY += valueY;
