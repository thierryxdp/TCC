def uppCons(frase):
    '''Uma função que recebe uma frase e deixa as cosoantes
    maiúsculas e os demais caracteres na forma original
    str -> str'''
    c = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            c += caractere.upper() 
        else:
            c += caractere
    return c