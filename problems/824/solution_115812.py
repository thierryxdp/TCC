def uppCons(frase):
    '''Retorna a frase com todas as consoantes em maiúsculas
str -> str'''
    i=0
    novafrase=''
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            novafrase=novafrase+str.upper(frase[i])
        else:
            novafrase=novafrase+frase[i]
        i=i+1
    return novafrase