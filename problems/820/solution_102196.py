def posLetra(string, letra, posicao):
    cont = 0
    for n in range(len(string)):
        if string[n] == letra:
            cont+=1
        if cont == posicao:
            return n
    return -1