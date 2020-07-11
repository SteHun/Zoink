def save(path, content):
    try:
        with open(path, 'w') as file:
            file.write(content)
    except:
        with open(path, 'wb') as file:
            file.write(content)

def read(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except:
        with open(path, 'rb') as file:
            return file.read()