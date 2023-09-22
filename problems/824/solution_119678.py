def uppCons (frase):
    '''retorna, com todas as consoantes em maiusculas, uma frase de entrada 
    str -> str'''
    i = 0
    while i<len(frase):
        if not frase[i] in 'AEIOUaeiou':
        frase = frase.upper([i])
    return frase