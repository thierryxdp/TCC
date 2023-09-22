def uppCons(frase):
    indice = 0
    vogais = 'aeiou'
    frase_final = ''

    while indice < len(frase):
        if frase[indice] not in vogais:
            frase_final += frase[indice].upper()
            indice += 1

        else:
            frase_final += frase[indice]
            indice += 1

    return frase_final