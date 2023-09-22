def uppCons(frase):
    '''Esta função recebe ma frase e retorna ela com todas as consoantes em letra maiúscula.
str->str'''
    i=0
    while i<len(frase):
        if frase[i]!='aeiou':
            a=frase[i].upper()
        i=i+1
    return a