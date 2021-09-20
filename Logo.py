class Logo(object):

    def __init__(self,screen,imagesObject,x,y):
        self.__mainScreen = screen;
        self.__imagesObject = imagesObject;
        self.__x = x;
        self.__y = y;

    def draw(self):
        self.__mainScreen.blit(self.__imagesObject.logo_Image,(self.__x,self.__y));
