def save(path, content):#requires full path
    if (not path.startswith("C:\\Users\\")) and path.startswith('C:'):
        raise RuntimeError(f'this will harm your computer!!! You are trying to write to {path}')
    try:
        with open(path, 'w') as file:
            file.write(content)
    except:
        with open(path, 'wb') as file:
            file.write(content)

def read(path):#requires full path
    try:
        with open(path, 'r') as file:
            return file.read()
    except:
        with open(path, 'rb') as file:
            return file.read()