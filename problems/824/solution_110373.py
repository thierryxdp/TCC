def uppCons(frase):
    '''retorna uma frase com todas as consoantes maisculas
    str -> str'''
    i=0
    vogais = 'aeiouAEIOUãâéíóôúÃÂÉÍÓÚÔ'
    
    while i < len(frase):
        if (frase[i] not in vogais):
            frase = frase.replace(frase[i], frase[i].upper(), 1)
        i = i + 1

    return frase