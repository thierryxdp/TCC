def posLetra(palavra,letra,n):
    x = str.find(palavra,letra)
    while n > 1:
        x = str.find(palavra,letra + 1)
        n -= 1
    return x