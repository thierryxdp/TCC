def posLetra(string,letra,numero):
    inicio = 0
    indexes = []
    while inicio < len(a):
        resultado = a.find(termo, inicio)
        if resultado == -1: 
            break
        indexes.append(resultado)
        inicio = resultado + 1
    return indexes