def posLetra(frase,letra,num):
    if (num <= str.count(frase,letra)):
        return str.index(frase,letra,num,-1)
    else:
        return -1