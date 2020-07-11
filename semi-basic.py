import basic

def compare(path1, path2):
    if basic.read(path1) == basic.read(path2):
        return True
    else:
        return False