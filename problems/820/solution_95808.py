def posLetra(frase, letra, vezes):
    i = 0
    aux = 0
    while aux < len(frase):
        if frase[aux] == letra:
            if i == vezes:
                return aux
            else :
                i += 1
                
        aux += 1

    return aux-1