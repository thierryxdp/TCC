def posLetra(frase,letra,n):
    i = 0
    inicio = 0
    while i<n:
        inicio = str.find(frase,letra,inicio)
        i = i + 1
    return inicio