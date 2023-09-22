def uppCons(frase):
    prox = 0
    fraseLista = []
    while prox < len(frase):
        if frase[prox] != 'AEIOUaeiou':
            list.append(fraseLista, frase[prox].upper())
        prox = prox + 1
    return ''.join(fraseLista)