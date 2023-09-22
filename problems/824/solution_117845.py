def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    i = 0
    oracao = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            oracao = str.upper(oracao) + frase[i]
        i = i + 1
    return oracao