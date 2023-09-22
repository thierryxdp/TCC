def uppCons(frase):
    '''função que a partir de uma frase, retorna a mesma com as consoantes em maiúsculo; str -> str'''
    
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.upper(frase[i])
        i = i+1
    return frase