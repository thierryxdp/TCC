def uppCons(frase):
    '''Dada uma frase, retorna a mesma frase com as consoantes maiusculas
    str->str'''
    i=o
    frase=str.upper(frase)
    while i<len(frase):
        if frase[i] in 'AEIOU':
            str.replace(frase,(frase[i]),(str.lower(frase[i]))
     i=i+1
    return frase