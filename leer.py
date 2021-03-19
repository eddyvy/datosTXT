import re

def leer():
    f = open('datos.txt', 'r')
    x = f.read()
    y = re.findall(" id: \d+", x)
    print(len(y))
    f.close()


if __name__ == '__main__':
    leer()