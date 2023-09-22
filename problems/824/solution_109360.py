def uppCons(frase):
    proximo = 0
    nova_frase = ''
    while proximo < len(frase):
        if frase[proximo] != 'a' and frase[proximo] != 'e' and frase[proximo] != 'i' and frase[proximo] != 'o' and frase[proximo] != 'u':
            nova_frase += frase[proximo].upper()
        else:
            nova_frase += frase[proximo]
        proximo = proximo + 1
    return nova_frase