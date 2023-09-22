def uppCons(frase):
    """Tem como objetivo receber uma frase e retornar
    todas as consoantes da frase em maiúsculo.
    str > str"""
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s
    return(consoantes_maiusculas('abcdef'))