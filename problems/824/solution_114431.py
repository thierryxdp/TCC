def uppCons(frase):
    '''ao receber uma frase, retorna a mesma frase, porém
    com as consoantes em maiúscula.
    str -> str'''
    frase = list(frase)
    prox = 0
    fraseLista = []
    vogais = 'aeiouAEIOU'
    while prox < len(frase):
        if vogais not in frase[prox]:
            letra = frase[prox].upper()
            list.append(fraseLista, letra)
        prox = prox + 1
    return ''.join(fraseLista)