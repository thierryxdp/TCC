def uppCons(frase):
    '''Dada uma frase, retorna a mesma frase com as consoantes maiusculas
    str->str'''
    i=0
    frase=str.upper(frase)
    while i<len(frase):
        if frase[i] in 'AEIOU':
            str.replace(frase,(frase[i]),(str.lower(frase[i])))
        i=i+1
    return frase