def posLetra(string,letra,num):
    if string.count(letra) >= num:
        return string.find(letra)
    else:
        return -1