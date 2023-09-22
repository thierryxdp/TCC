def posLetra(texto,letra,numero):
    x = 0
    while x < numero:
        indice = str.find(texto,letra,x)
        x=x+1
    return indice