def lingua_p(frase):
    '''Uma função que recebe uma frase e após uma vogal
    recebe "p" mais a vogal e os demais caracteres na forma original
    str -> str'''
    c = ''
    for letra in frase:
        if letra in 'aeiouáéíóú':
            c += letra +'p'+ letra
        else:
            c += letra
    return c