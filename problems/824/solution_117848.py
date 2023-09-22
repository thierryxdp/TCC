def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    i = 0
    maiuscula = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(maiuscula)+frase[i]
        i = i + 1
    return str(maiuscula)