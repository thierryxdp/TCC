def posLetra(frase,letra,num):
    x = 0
    tem = 0
    while x < len(frase) and tem != num:
        if frase[x] == letra:
            tem = tem + 1
            x = x + 1
        else:
            x = x + 1
    if tem >= num:
        return x-1
    else:
        return -1