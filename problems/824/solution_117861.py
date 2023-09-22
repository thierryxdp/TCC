def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    maiuscula = ''
    while maiuscula<len(frase):
        if maiuscula in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(maiuscula)
    return maiuscula