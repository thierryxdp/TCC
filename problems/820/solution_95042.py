def posLetra(string,letra,numero):
    inicio = 0
    indexes = []
    while inicio < len(string):
        resultado = string.find(letra, inicio)
        if resultado == -1: 
            break
        indexes.append(resultado)
        inicio = resultado + 1
    return indexes[numero]-1