def uppCons(frase):
    '''Esta função recebe ma frase e retorna ela com todas as consoantes em letra maiúscula.
str->str'''
    i=0
    a=''
    consoantes='bcdfghjklmnpqrstvwxyzç'
    while i<len(frase):
        letra=frase[i]
        if letra in consoantes:
            letra= str.upper(letra)
        a+=letra
        i=i+1
    return  a