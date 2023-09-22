def uppCons (frase):
    '''...'''
    r = ''
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    
    for caractere in frase:
        if caractere in consoantes:
            r += caractere.upper()
        else:
            r += caractere
    return r