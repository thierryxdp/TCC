def posLetra(frase, letra, vezes):
    aux = 0

    for i in range(len(frase)):
        if frase[i] == letra:
            if aux == vezes:
                return i
            else :
                aux += 1

    return -1