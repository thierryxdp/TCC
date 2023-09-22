def uppCons(frase):
    '''A função retornará a frase inserida com todas as consoantes em maiúsculo. As outras letras retornarão
    conforme elas foram inseridas
    dados de entrada -> string
    dados de saída -> string'''
    
    Q = len(frase)
    novafrase = ''
    i = 0
    
    while i < Q:
        if frase[i] in 'bcçdfghjklmnpqrstvwxz':
            novafrase = novafrase + str.upper(frase[i])
        else:
            novafrase = novafrase + frase[i]
        i = i + 1
    return novafrase