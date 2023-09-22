def posLetra(string,letra,numero):
    inicio = 0
    indexes = []
    while inicio < len(string):
        resultado = string[inicio:].find(letra)
    if resultado == -1: 
        return -1
    indexes.append(resultado + inicio)
    inicio += resultado + 1