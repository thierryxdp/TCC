def uppCons(frase):
    'retorna a frase com as consoantes maisuculas'
    'string----string'
    novafrase=''
    for letra in frase:
        if letra.lower()in'bcçdfghjklmnpqrstvwyz':
            novafrase+=letra.upper()
        else:
            novafrase+=letra
    return novafrase