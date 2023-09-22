def uppCons(frase):
    '''Função que recebe uma frase como entrada e retornará a mesma frase, apenas com as consoantes em maiúsculas. str -> str'''
    i=0
    f=frase.split()
    while i<len(f):
        if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz'):
            f[i]=str.upper(f[i])
            del f[i+1]            
            i=i+1
    return str.join(f)