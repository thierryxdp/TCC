def consoantes_maiusculas(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() # transforma em maiúscula
        else: # não é consoante minúscula, mantém como no original
            s += caractere
    return s

print(consoantes_maiusculas('abcdef')) # aBCDeF