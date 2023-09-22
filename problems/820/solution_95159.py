def posLetra (string, letra, num):
    i = 0
    while i < len(string):
        if string.count(letra) >= num:
            return string.index(letra,num)
        else:
            return -1