def uppCons(frase):
    '''Função que recebe uma frase e retorne ela mesma com suas
    consoantes em maiúsculas'''
    i = 0

    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUãáàéèíóôú':
            frase = frase.replace(frase[i],frase[i].upper())
        i = i+ 1
    return frase