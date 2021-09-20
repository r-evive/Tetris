import sys,os;

class Resource():

    def createPath(path):
        try:
            base_path = sys._MEIPASS;
        except Exception:
            base_path = os.path.abspath(".");

        return os.path.join(base_path, path);