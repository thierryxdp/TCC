def uppCons(frase):
    nova_frase = ''
    for letra in frase.upper():
        if letra in 'AEIOU':
            nova_frase += letra.lower()
        else:
            nova_frase += letra