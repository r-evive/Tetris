from Data import *;
from pathlib import Path;
import os, pickle;

class Ranking(object):
    
    def __init__(self):
        self.__ranking = {"name":None, "points":0};
        self.__ranking.clear();

    def saveCurrentStats(self):
        if(Data.nickname in  self.__ranking):
            if(self.__ranking[Data.nickname] < Data.points):
                self.__ranking[Data.nickname] = Data.points;
        else:
            self.__ranking[Data.nickname] = Data.points;

        with open("C:\\Users\\Public\\ranking.txt","wb") as filehandler:
            pickle.dump(self.__ranking, filehandler);

    def readStats(self):
        plik = Path("C:\\Users\\Public\\ranking.txt");
        if(plik.exists()):
            with open("C:\\Users\\Public\\ranking.txt","rb") as filehandler:
                self.__ranking = pickle.load(filehandler);


    def getArray(self):
        return self.__ranking;