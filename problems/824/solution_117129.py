def uppCons(frase):
    '''função que recebe uma frase como entrada e retorna
a mesma frase, porém com todas suas consoantes maiúsculas.
str -> str'''
    s=''
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvwxyz':
            s=s+str.upper(frase[i])
        else:
            s=s+str(frase[i])
        i=i+1
    return s