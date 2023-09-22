def uppCons(frase):
    '''A função retornará a frase inserida com todas as consoantes em maiúsculo. As outras letras retornarão
    conforme elas foram inseridas'''
    
    Q = len(frase)
    novafrase = ''
    i = 0
    
    while i < Q:
        if frase[i] in 'bcdfgjklmnpqrstvwxz':
            novafrase = novafrase + str.upper(frase[i])
        else:
            novafrase = novafrase + frase[i]
    return novafrase