def uppCons(frase):
    '''ao receber uma frase, retorna a mesma frase, porém
    com as consoantes em maiúscula.
    str -> str'''
    frase = list(frase)
    prox = 0
    fraseLista = []
    while prox < len(frase):
        if frase[prox] not in 'aeiouAEIOU':
            letra = frase[prox].upper()
            list.append(fraseLista, letra)
        else:
            letra = frase[prox]
            list.append(fraseLista, letra
        prox = prox + 1
    return ''.join(fraseLista)