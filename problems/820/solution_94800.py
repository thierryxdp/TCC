def posLetra(frase, letra, ocorr):
    cont = 0
    exist = 0
    pos = 0

    while cont < len(frase) and exist < ocorr:
        if frase[cont] == letra:
            exist +=  1
            pos = cont
            
        cont += 1

    if exist < 0:
        return -1
    else:
        return pos