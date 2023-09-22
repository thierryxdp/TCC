def uppCons(frase):
    '''função que retorna todas as consoantes em maiúsculas. str -> str'''
    i=0
    while i<len(frase):
        if frase [i] in 'bcdfghjklmnpqrstvxwyz':
            frase_mai = frase_mai+(str.upper(frase[i]))
        else:
            frase_mai = frase_mai + frase[i]
        i=i+1
    return frase_mai