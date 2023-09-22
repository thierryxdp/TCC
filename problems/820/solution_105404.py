def posLetra(texto,letra,numero):
    x = 0
    indice = str.find(texto,letra)
    while x < numero:
        indice = str.find(texto,letra,x+1)
        x=x+1
    return indice