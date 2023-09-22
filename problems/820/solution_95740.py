def posLetra(frase, letra, vezes):
    auc = 0

    for i in range(frase):
        if frase[aux] == letra:
            if aux == vezes:
                return i
            else :
                aux += 1

    return -1