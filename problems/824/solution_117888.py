def uppCons(frase):
    '''Função que retorne todas as consoantes maiúsculas, str -> str'''
    x = 0
    oracao = ''
    while x<len(frase):
        if maiuscula in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(maiuscula)
            oracao = oracao + maiuscula
        x = x + 1
    return oracao