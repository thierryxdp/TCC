def uppCons(frase):
    "retorna as consoantes da string orginal em consoantes maiusculas"
    s = ''
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper()
        else: 
            s += caractere
    return s