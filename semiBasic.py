import basic
import os

#full path example: C:\users\<username>\desktop\testdir\dir\file.txt
#base path example: C:\users\<username>\desktop\testdir\
#relative path example: dir\file.txt

def compare(path1, path2):#requires full paths
    if basic.read(path1) == basic.read(path2):
        return True
    else:
        return False

def index(dir):#requires base path, returns full paths
    output = []
    for x in os.listdir(dir):
        if os.path.isdir(dir + '\\' + x):
            output += index(dir + '\\' + x)
        else:
            output.append(dir + '\\' + x)
    return output

def dirIndex(dir):#requires base path, returns full paths
    output = []
    for x in os.listdir(dir):
        if os.path.isdir(dir + '\\' + x):
            output.append(dir + '\\' + x)
            output += dirIndex(dir + '\\' + x)
    return output

def convertToRelative(basePath, fullPath):
    if fullPath.startswith(basePath):
        output = fullPath[len(basePath):len(fullPath)]
        return output
    else:
        raise RuntimeError('fullPath does not start with basePath')

def decideAction(originalRelativePath, originalBasePath, targetRelativePath, targetBasePath):#returns string 'overwrite', 'remove' or 'keep'
    