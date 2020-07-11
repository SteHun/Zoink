import basic
import os

def compare(path1, path2):
    if basic.read(path1) == basic.read(path2):
        return True
    else:
        return False

def index(dir):
    output = []
    for x in os.listdir(dir):
        if os.path.isdir(dir + '\\' + x):
            output += index(dir + '\\' + x)
        else:
            output.append(dir + '\\' + x)
    return output

def dirIndex(dir):
    output = []
    for x in os.listdir(dir):
        if os.path.isdir(dir + '\\' + x):
            output.append(dir + '\\' + x)
            output += dirIndex(dir + '\\' + x)
    return output

