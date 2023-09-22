def uppCons(frase):
    '''Função que recebe uma frase como entrada e retornará a mesma frase, apenas com as consoantes em maiúsculas. str -> str'''
    i=0
    f=frase
    while i<len(f):
        if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz'):
            f[i:i+1]
           	str.upper(f[i])+f
            i=i+1
    return f