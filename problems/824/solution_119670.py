def uppCons(frase):
    '''retorna a frase com as consoantes em maiúsculas;
str->str'''
    novafrase=''
    i=0

    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            novafrase= novafrase + str.upper(frase[i])
        else:
            novafrase= novafrase + frase[i]
        i=i+1
    return novafrase