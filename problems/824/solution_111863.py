def uppCons (frase):
    '''...'''
    
    s = ''
    consoantes = 'bcdfghjklmnpqrstuvwxyz'
    
    for caractere in frase:
        if caractere in consoantes:
            s += caractere.upper()
        else:
            s += caractere
    return frase