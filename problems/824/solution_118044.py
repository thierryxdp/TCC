def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'BCDFGHJKLMNPQRSTVXWYZbcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else: 
            s += caractere
    return s

print(consoantes_maiusculas('abcdef'))