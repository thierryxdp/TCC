def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    x = 0
    maiuscula = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(maiuscula, frase[i])
        x = x + 1
    return str(maiuscula)