def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    maiuscula = ''
    while x<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(frase[1])
    return maiuscula