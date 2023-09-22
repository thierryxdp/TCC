def uppCons(frase):
    '''retorna a frase com todas as consoantes maisculas
str -> str'''
    i=0
    nova_frase=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            nova_frase=nova_frase+str.upper(frase[i])
        else:
            nova_frase=nova_frase+frase[i]
        i=i+1
    return nova_frase