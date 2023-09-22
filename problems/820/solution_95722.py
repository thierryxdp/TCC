def posLetra(frase,letra,num):
    if (num <= str.count(frase,letra)):
        return str.index(frase,letra,num)
    else:
        return -1