def uppCons(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else: 
            s += caractere
    return s

print(uppCons('abcdef'))