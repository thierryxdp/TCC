def posLetra(palavra,letra,n):
    pos = str.find(palavra,letra)
    while n > 1:
        pos = str.find(palavra,letra, x+ 1)
        n -= 1
    return x