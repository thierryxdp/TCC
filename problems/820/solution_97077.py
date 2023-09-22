def posLetra(string,letra,num):
    if string.find(letra) >= num:
        return string.find(letra)
    else:
        return -1