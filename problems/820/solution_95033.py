def posLetra(string,letra,numero):
    inicio = 0
    termo =letra
    indexes = []
    while inicio < len(string):
        resultado = string[inicio:].find(termo)
    if resultado == -1: 
        return -1
    indexes.append(resultado + inicio)
    inicio += resultado + 1