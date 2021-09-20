import pygame, threading;
from Image import *;
from Background import *;
from Menu import *;
from Game import *;
from Ranking import *;

class MainWindow(object):
    __width = int();
    __height = int();
    __running = False;
    __x = 0;
    __FPS = 60;
    __mainScreen = pygame.display;
    __loopThread = threading.Thread();
    __images = None;
    __mainClock = pygame.time.Clock();
    __background = Background(None, None);
    __menu = None;
    __currentMode = "Start";
    __game = None;

    @property
    def Width(self):
        return self.__width;    

    @Width.setter
    def Width(self, width):
        self.__width = width;

    def __mainLoop(self):
        while(self.__running):
            self.__background.draw();
            self.__menu.draw();
            self.__game.draw();
            for event in pygame.event.get():
                self.__menu.Handler(event);
                self.__game.Handler(event);
                if event.type == pygame.QUIT:
                    self.__running = False;

            self.__mainClock.tick(self.__FPS);
            pygame.display.set_caption("FPS: "+ str(float("{0:.2f}".format(self.__mainClock.get_fps()))));
            pygame.display.update();

    def stop(self):
        self.__running = False;

    def __setMode(self,mode):
        self.__currentMode = mode;

    def __getMode(self):
        return self.__currentMode;
    def __init__(self,width,height):
        pygame.init();
        self.__width = width;
        self.__height = height;
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.__mainScreen = pygame.display.set_mode((width, height),pygame.DOUBLEBUF | pygame.HWSURFACE);
        self.__images = Image(self.__mainScreen);
        self.__background = Background(self.__mainScreen,self.__images);
        self.__ranking = Ranking();
        self.__menu = Menu(self.__mainScreen,self.__images,108,275,self.stop, self.__ranking);
        self.__game = Game(self.__mainScreen,self.__images,self.__ranking,0,0);
        pygame.key.set_repeat(70,32);
        self.__running = True;
        self.__loopThread = threading.Thread(target = self.__mainLoop());
        self.__loopThread.setDaemon(True);
        self.__loopThread.start();


