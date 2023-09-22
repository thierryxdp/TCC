def uppCons(frase):
    '''Faça uma função que retorne todas as suas consoantes maiúsculas, str -> str'''
    i = 0
    maiuscula = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            oracao = str.upper(maiuscula)+frase[i]
        i = i + 1
    return str(oracao)