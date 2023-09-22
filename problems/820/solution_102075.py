def posLetra(string, letra, numero):
    contador = numero
    certo = False
    while contador < len(string) and not certo:
        if string[contador] == letra:
            certo = True
        else:
            contador = contador + 1
    if numero >= string.count(letra):
        return contador
    else:
        return -1