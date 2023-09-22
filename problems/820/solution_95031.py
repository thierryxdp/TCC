def posLetra(string,letra,numero):
    inicio = 0
    termo =l
    indexes = []
    while inicio < len(string):
        resultado = string[inicio:].find(termo)
    if resultado == -1: 
        break
    indexes.append(resultado + inicio)
    inicio += resultado + 1