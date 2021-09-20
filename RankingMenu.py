import pygame;
import operator;
from Button import *;
from Data import *;

class RankingMenu(object):
    def __init__(self, mainScreen, imagesObject, ranking):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__ranking = ranking;
        self.__x = 190;
        self.__y = 50;
        self.__font = pygame.font.SysFont('freesansbold.ttf',32);
        self.__firstPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+100,None);
        self.__secondPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+150,None);
        self.__thirdPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+200,None);
        self.__fourthPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+250,None);
        self.__fifthPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+300,None);
        self.__sixthPlace = Button(self.__mainScreen,self.__imagesObject.rankingListElementOn,self.__imagesObject.rankingListElementOff,self.__x-70,self.__y+350,None);
        self.__backButton = Button(self.__mainScreen,self.__imagesObject.backButtonOn, self.__imagesObject.backButtonOff,self.__x-50,self.__y + 500,self.__backMethod);
    
    def Handler(self,event):
        self.__firstPlace.Handler(event);
        self.__secondPlace.Handler(event);
        self.__thirdPlace.Handler(event);
        self.__fourthPlace.Handler(event);
        self.__fifthPlace.Handler(event);
        self.__sixthPlace.Handler(event);
        self.__backButton.Handler(event);

    def __backMethod(self):
        Data.currentMode = "Menu";

    def draw(self):
        self.__ranking.readStats();
        rankingSorted = sorted(self.__ranking.getArray().items(), key=operator.itemgetter(1),reverse = True);
        self.__mainScreen.blit(self.__imagesObject.rankingImage,(self.__x-70,self.__y));
        self.__backButton.draw();

        if(len(rankingSorted)<6):
            for i in range(len(rankingSorted)):
                if(i==0):
                    if(self.__firstPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__firstPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));
                elif(i==1):
                    if(self.__secondPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__secondPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));
                elif(i==2):
                    if(self.__thirdPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__thirdPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));
                elif(i==3):
                    if(self.__fourthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__fourthPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));
                elif(i==4):
                    if(self.__fifthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__fifthPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));
                elif(i==5):
                    if(self.__sixthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                    text = self.__font.render(input, True, (255, 255, 255));
                    self.__sixthPlace.draw();
                    self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));

        else:
            self.__firstPlace.draw();
            self.__secondPlace.draw();
            self.__thirdPlace.draw();
            self.__fourthPlace.draw();
            self.__fifthPlace.draw();
            self.__sixthPlace.draw();
            for i in range(0,6,1):
                if(i==0):
                    if(self.__firstPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                elif(i==1):
                    if(self.__secondPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                elif(i==2):
                    if(self.__thirdPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                elif(i==3):
                    if(self.__fourthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                elif(i==4):
                    if(self.__fifthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                elif(i==5):
                    if(self.__sixthPlace.mouseAbove):
                        input = str(rankingSorted[i][1]) + " pkt.";
                    else:
                        input = str(i+1)+ ". "+ str(rankingSorted[i][0]);
                text = self.__font.render(input, True, (255, 255, 255));
                self.__mainScreen.blit(text,(self.__x-65 + self.__imagesObject.rankingListElementOff.get_size()[0]/2 - len(input)*6,self.__y+113+i*50));

