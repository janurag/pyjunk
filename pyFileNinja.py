import os
try:
    from os import scandir
except ImportError:
    # print "Importing Exception  > scandir"
    from scandir import scandir # pip install scandir

# from pathlib import Path



class pyFileNinjaClass():
    def __init__(self):
        self.everything = scandir()
        self.file_list = []
        self.directory_list = []
        for _ in self.everything:
                if _.is_file():
                    self.file_list.append(_.name)
                elif _.is_dir():
                    self.directory_list.append(_.name)
                    

    def files(self):
        return self.file_list
    
    def dirs(self):
        return self.directory_list

if __name__ == "__main__":
    pyfile = pyFileNinjaClass()
    print pyfile.files()