def uppCons(frase):
    ''' Funcao que recebe uma frase e retorna todas as consoantes maiusculas
str->str'''
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
           str.upper(frase[i]) 
        i=i+1
        return frase