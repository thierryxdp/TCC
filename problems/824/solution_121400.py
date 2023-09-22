def uppCons(frase):
    frase_alterada= ""
    proximo= 0
    while proximo<len(frase):
        if frase[proximo] not in "aeiouAEIOU":
            frase_alterada = frase.upper()
        proximo= proximo + 1
    return frase_alterada