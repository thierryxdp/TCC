def uppCons(frase):
    '''Uma função que recebe uma frase e deixa as cosoantes
    maiúsculas e os demais caracteres na forma original
    str -> str'''
    c = ''
    while letra in frase:
        if letra in 'bcdfghjklmnpqrstvxwyzç':
            c += letra.upper() 
        else:
            c += letra
    return c