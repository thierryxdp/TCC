def posLetra(palavra,letra,n):
    pos = str.find(palavra,letra)
    while n > 1:
        pos = str.find(palavra,letra, pos+ 1)
        n -= 1
    return pos