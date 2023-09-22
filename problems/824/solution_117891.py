def uppCons(frase):
    '''Função que retorne todas as consoantes maiúsculas, str -> str'''
    x = 0
    oracao = ''
    while x<len(frase):
        maiuscula = frase[x]
        if maiuscula in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(maiuscula)
        oracao = oracao + maiuscula
        x = x + 1
    return oracao