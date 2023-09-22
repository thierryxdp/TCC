def uppCons(frase):
    '''Recebe de entrada uma frase e retornar todas suas consoantes em maiusculo
    str -> str'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s