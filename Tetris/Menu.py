from Button import *;
from Logo import *;
from InputBox import *;
from RankingMenu import *;

class Menu(object):

    __moving = False;
    __xValue = 0;
    __yValue = 0;

    def __init__(self,mainScreen,imagesObject,x,y,stopMethod, ranking):
        self.__x = x;
        self.__y = y;
        self.__stopMethod = stopMethod;
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__startButton = Button(self.__mainScreen,self.__imagesObject.start_on_Image,self.__imagesObject.start_off_Image,self.__x + 35,self.__y,self.__startButtonEvent);
        self.__rankingButton = Button(self.__mainScreen,self.__imagesObject.ranking_on_Image,self.__imagesObject.ranking_off_Image,self.__x + 35,self.__y + self.__imagesObject.ranking_off_Image.get_size()[1] + 25,self.__rankingButtonEvent);
        self.__exitButton = Button(self.__mainScreen,self.__imagesObject.exit_on_Image,self.__imagesObject.exit_off_Image,self.__x+35,self.__y + self.__imagesObject.exit_off_Image.get_size()[1]+ self.__imagesObject.options_off_Image.get_size()[1] + 25*2,self.__stopButtonEvent);
        self.__logo = Logo(self.__mainScreen,self.__imagesObject,self.__x-25,self.__y-165);
        self.__inputBox = InputBox(self.__mainScreen,self.__imagesObject.textInput_Image,108,200);
        self.__nextButton = Button(self.__mainScreen,self.__imagesObject.next_on_Image,self.__imagesObject.next_off_Image,140,340,self.__nextButtonEvent);
        self.__ranking = ranking;
        self.__ranking.readStats();
        self.__rankingMenu = RankingMenu(self.__mainScreen,self.__imagesObject,self.__ranking);

    def Handler(self,event):
        if(Data.currentMode == "Menu"):
            self.__startButton.Handler(event);
            self.__exitButton.Handler(event);
            self.__rankingButton.Handler(event);
        elif(Data.currentMode == "Start"):
            self.__inputBox.Handler(event);
            self.__nextButton.Handler(event);
        elif(Data.currentMode == "Ranking"):
            self.__rankingMenu.Handler(event);

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if(Data.currentMode == "Game" or Data.currentMode== "Ranking"):
                    Data.currentMode = "Menu";
                    self.visible = True;
                    self.enabled = True;
                    self.logoVisible = True;
                    pygame.mouse.set_visible(True);
                    
    def draw(self):
        if(Data.currentMode == "Menu"):
            self.__startButton.draw();
            self.__rankingButton.draw();
            self.__exitButton.draw();

        if(Data.currentMode == "Menu"):
            self.__logo.draw();
        if(Data.currentMode == "Start"):
            self.__inputBox.draw();
            self.__nextButton.draw();
        if(Data.currentMode == "Ranking"):
            self.__rankingMenu.draw();


    def move(self, xValue, yValue):
        self.__xValue = xValue;
        self.__yValue = yValue;
        self.__moving = True;

    def __startButtonEvent(self):
        pygame.mouse.set_visible(False);
        Data.currentMode = "Game";


    def __stopButtonEvent(self):
        self.__stopMethod();
        
    def __rankingButtonEvent(self):
        Data.currentMode = "Ranking";


    def __nextButtonEvent(self):
        if(len(Data.nickname)>2):
            Data.currentMode = "Menu";