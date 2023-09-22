def uppCons(frase):
    '''função que recebe uma frase como entrada e retorna
a mesma frase, porém com todas suas consoantes maiúsculas.
str -> str'''
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
        i=i+1
     return frase