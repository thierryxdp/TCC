def posLetra(x, y, z):
    #x = palavra
    #y = item
    #z = repeticao
    #procurar a letra nesta palavra
    achar = x.find(y)
    #correr a string para poder procurar mais de uma vez, caso haja mais de uma ocorrência
    while achar >= 0 and z > 1:
        achar = x.find(y, achar+1)
        z -= 1
    return achar