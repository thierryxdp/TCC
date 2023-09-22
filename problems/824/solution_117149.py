def uppCons(frase):
    nova_frase = ''
    for letra in frase.upper():
        if letra in 'AEIOUÃÚÓÉÁÔ':
            nova_frase += letra.lower()
        else:
            nova_frase += letra
    return nova_frase