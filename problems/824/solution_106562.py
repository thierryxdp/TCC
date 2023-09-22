def uppCons(frase):
    '''Dada uma frase, retorna a mesma, com todas as consoantes em maiúsculo'''
    '''str->str'''
    x=0
    while x<len(frase):
        if frase[x] not in 'AEIOUaeiou':
            str.upper(frase[x])
        x=x+1
    return frase