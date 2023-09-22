def posLetra(frase, letra, vezes):
    aux = 0

    for i in range(len(frase)):
        if frase[i] == letra:
            aux += 1

            if aux == vezes:
                return i
            
    return -1