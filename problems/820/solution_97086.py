def posLetra(string,letra,num):
    while string.count(letra) >= num:
        if string.count(letra) = 2:
            x = string.find(letra) + 1
            y = string.find(letra[x:])
            return y
        if string.count(letra) = 3:
            z = string.find(letra[y:])
            return z
    return string.find(letra)
    else:
        return -1