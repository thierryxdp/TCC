def uppCons(frase):
    nova_frase = ''
    for letraMai, letraOrig in zip(frase.upper(),frase):
        if letraMai not in 'AEIOUÃÚÓÉÁÔÍ':
            nova_frase += letraMai
        else:
            nova_frase += letraOrig
    return nova_frase