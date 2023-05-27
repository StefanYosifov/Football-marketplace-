import os


full_path = os.path.realpath(__file__)
print(full_path)

def getCurrentDirectory():
    return os.path.dirname(full_path)

def getImage(path):
    return getDirectoryTwoBack()+path

def getDirectoryTwoBack():
    return os.path.abspath(os.path.join(__file__ ,"../.."))


 