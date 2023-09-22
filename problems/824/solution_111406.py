def uppCons(frase):
    '''função que recebe uma frase e retorna essa mesma frase 
    so que as consoantes em maiuscula'''
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s