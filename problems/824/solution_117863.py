def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    x = 0
    maiuscula = ''
    while frase[x]<len(frase):
        if frase[x] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = maiuscula + str.upper(frase[x])
    x = x + 1 
    return str(maiuscula)