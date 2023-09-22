def posLetra(frase, letra, ind):
    pos_letra = 0
    if ind <= frase.count(letra):
        while pos_letra < frase.count(letra):
            pos_letra += 1
        return pos_letra 
    else:
        return -1