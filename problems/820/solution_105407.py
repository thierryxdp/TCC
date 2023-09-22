def posLetra(texto,letra,numero):
    x = 0
    indice = str.find(texto,letra)
    if indice == -1:
        return indice
    x = 1
    while x < numero:
        indice = str.find(texto,letra,x+1)
        if indice == -1:
        	return indice
        x=x+1
    return indice