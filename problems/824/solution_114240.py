def uppCons(frase):
    '''Dada uma frase, retorna esta frase com todas as suas
    consoantes em maiúsculas.
    str -> str'''
    indice = 0
    FRASE = ''
    while indice < len(frase):
        if frase[indice] in 'bcçdfghjklmnñpqrstvwxyz':
            FRASE = FRASE + str.upper(frase[indice])
        else:
            FRASE = FRASE + frase[indice]
        indice = indice + 1
    return FRASE