def posLetra(string, letra, numero):
    contador = numero
    certo = False
    while contador < len(string) and not certo:
        if string[contador] == letra:
            certo = True
        else:
            contador = contador + 1
    if certo:
        return contador
    else:
        return -1