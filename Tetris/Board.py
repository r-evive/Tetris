class Board(object):

    def __init__(self,mainScreen,imagesObject,x,y):
        self.__mainScreen = mainScreen;
        self.__imagesObject = imagesObject;
        self.__x = x;
        self.__y = y;


    def draw(self):
        self.__mainScreen.blit(self.__imagesObject.board_Image,(self.__x,self.__y));