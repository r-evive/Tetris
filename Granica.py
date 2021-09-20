class Granica(object):

    def __init__(self, X, Y, width, height):
        self.__width = width;
        self.__height = height;
        self.__X = X;
        self.__Y = Y;

    @property
    def Width(self):
        return self.__width;
    @property
    def Height(self):
        return self.__height;
    @property
    def X(self):
        return self.__X;
    @property
    def Y(self):
        return self.__Y;