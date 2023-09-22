def uppCons(frase):
    '''Dada uma frase retorna a mesma com suas consoantes maiúsculas 
    str -> str'''
    nFrase = ''
    c = 0
    while c < len(frase):
        if frase[c] in 'bcdfghjklmnpqrstvwxyzç':
            nFrase += str.upper(frase[c])
        else:
            nFrase += frase[c]
        c += 1
    return nFrase