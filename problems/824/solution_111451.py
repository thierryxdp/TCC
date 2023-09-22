def uppCons(frase):

    for i in frase:
        if i not in 'AEIOUaeiouãáéíóú':
            frase = frase[0:frase.index(i)] + i.upper() + \
                    frase[frase.index(i) + 1:]

    return frase