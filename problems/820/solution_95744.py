def posLetra(frase,letra,num):
    frse.strip()
    if (num <= str.count(frase,letra)):
        return str.index(frase,letra,num)
    else:
        return -1