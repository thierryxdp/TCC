def uppCons(frase):
    '''Uma função que recebe uma frase e deixa as cosoantes
    maiúsculas e os demais caracteres na forma original
    str -> str'''
    i=0
    while i < len(frase):
         if frase[i]in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
         i=+1
    return frase