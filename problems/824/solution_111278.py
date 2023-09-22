def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i]in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
        i=i+1
    return frase
def consoantes_maiusculas(frase):
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else: 
            s += caractere
    return s

print(consoantes_maiusculas('abcdef'))