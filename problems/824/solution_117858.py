def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    x = 0
    maiuscula = ''
    while x<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(frase[1])
        x = x + 1
    return str(maiuscula)