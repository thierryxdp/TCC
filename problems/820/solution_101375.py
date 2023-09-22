def posLetra(frase,letra,num):
    x = 0
    tem = 0
    pos = 0
    while x < len(frase):
        if frase[x] == letra:
            tem = tem + 1
            pos = pos+1
            x = x + 1
        else:
            x = x + 1
    if tem >= num:
        return pos
    else:
        return -1