def posLetra(string,letra,num):
    while string.count(letra) >= num:
        if string.count(letra) == 2:
            x = string.find(letra) + 1
            y = string.find(letra[x:])
            return y
        return string.find(letra)
    else:
        return -1