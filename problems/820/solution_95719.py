def posLetra(frase,letra,num):
    if (num <= str.count(frase,letra)):
        return str.index(frase,letra,num,-1)
    elif (str.count(frase,letra)==0):
        return -1
    else:
        return -1