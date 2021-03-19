import os
import re
import datetime


def getPath():
    actualPath = os.path.abspath(os.getcwd())
    newPath = os.path.join(actualPath, 'ficheros')
    
    if not os.path.exists(newPath):
        os.makedirs(newPath)

    return newPath


def siguienteId():
    u = open("datos.txt", "r")
    v = re.findall(" id: \d+", u.read())
    nextId = len(v) + 1
    u.close()
    return nextId
    

def escribirDatos():
    newId = str('%03d' % siguienteId())
    f = open("datos.txt", "a")
    f.write('{\n')

    print('Guardemos los datos ;D')
    f.write('    id: ' + newId + ',\n')
    f.write('    date: ' + str(datetime.datetime.now()) + ',\n')
    print('Título: ')
    titulo = input()
    f.write('    title: ' + titulo + ',\n')
    print('Descripción: ')
    descripcion = input()
    f.write('    description: ' + descripcion + ',\n')
    print('Email: ')
    email = input()
    f.write('    email: ' + email + ',\n')
    print('Usuario: ')
    usuario = input()
    f.write('    user: ' + usuario + ',\n')
    print('Contraseña: ')
    contrasena = input()
    f.write('    password: ' + contrasena + '\n')

    f.write('},\n')
    f.close()

    archivoName = newId + ' ' + titulo + '.txt'
    archivoPath = os.path.join(getPath(), archivoName)

    n = open(archivoPath, 'x')
    n.write('{\n')

    n.write('    id: ' + newId + ',\n')
    n.write('    date: ' + str(datetime.datetime.now()) + ',\n')
    n.write('    title: ' + titulo + ',\n')
    n.write('    description: ' + descripcion + ',\n')
    n.write('    email: ' + email + ',\n')
    n.write('    user: ' + usuario + ',\n')
    n.write('    password: ' + contrasena + '\n')

    n.write('}\n')
    n.close()
    

if __name__ == "__main__":
    repetir = 1

    while repetir:
        
        escribirDatos()
        print('¿Escribir más datos?')
        x = input('(s/n): ')
        
        if x == 's':
            repetir = 1
        else:
            repetir = 0
