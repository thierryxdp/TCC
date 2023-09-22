def posLetra(string, letra, numero):
    contador = 0
    while contador < len(string):
        if string(contador) == letra:
            contador = contador + 1
    return contador