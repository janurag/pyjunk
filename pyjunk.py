"""

    -=*=- coding: utf-8 -=*=-
    ====================================
    Python Advance Files Organizer
    ====================================
"""
import os
# try:
#     from os import scandir
# except ImportError:
#     # print "Importing Exception  > scandir"
#     from scandir import scandir

from pyFileNinja import pyFileNinjaClass
from pathlib import Path

# x= scandir()
# for i in x:
#     print i.is_dir()

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    # "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}


FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
# print FILE_FORMATS
# file_list  = []
# dir_list = []
# for _ in DIRECTORIES.keys():
    # dir_list.append(_)

# print "!!! dir_list ::>", dir_list

# scandir()
pyf = pyFileNinjaClass()
files = pyf.files()
dirs = pyf.dirs()
# print "pyFileNinja Files", files
print ">> pyFileNinja dirs:>", dirs

def organize_junk():
    for entry in files:
        # if entry.is_dir():
            # dir_list.append(entry.name)
            # continue
        # elif entry.is_file():
            # print ">>>> ITssss a file"
        file_path = Path(entry)
        # print file_path
        file_format = file_path.suffix.lower()
        # print "file_format:", file_format
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            print "directory_path>", directory_path, type(directory_path.name)
            # try:
            # print "dir_list ::>", dir_list
            if (directory_path.name not in dirs):
                print "DIR not present**************"
                directory_path.mkdir()
            else:
                print "DIR PRESENT #####"                
            file_path.rename(directory_path.joinpath(file_path))

    try:
        os.mkdir("OTHER-FILES")
    except:
        pass

    # for dir in scandir():
    #     try:
    #         if dir.is_dir():
    #             os.rmdir(dir)
    #         else:
    #             os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER-FILES/' + str(Path(dir)))
    #     except:
    #         pass


if __name__ == "__main__":
    organize_junk()