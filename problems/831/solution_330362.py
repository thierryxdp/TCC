def lingua_p(frase):
    '''Uma função que recebe uma frase e deixa as cosoantes
    maiúsculas e os demais caracteres na forma original
    str -> str'''
    c = ''
    for letra in frase:
        if letra in 'aeiou':
            c += 'p' 
        else:
            c += letra
    return c