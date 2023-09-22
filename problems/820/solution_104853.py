def posLetra(string,letra,posicao):
    contador = 0
    string = list(string)
    for i in range(len(string)):
        if string[i] == letra:
            contador += 1
    if contador == posicao:
        return contador
    else :
        return -1