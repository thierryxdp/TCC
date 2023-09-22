def posLetra(string,letra,num):
    while string.count(letra) >= num:
        return string.find(letra)