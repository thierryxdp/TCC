def uppCons(frase):
    '''Dada uma frase qualquer, a função retorna a frase
    com todas as suas consoantes em maiúsculo.
    str -> str'''
     s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s