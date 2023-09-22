def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghçjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s