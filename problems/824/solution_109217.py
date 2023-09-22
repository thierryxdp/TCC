def uppCons(frase):
    indice = 0
    consoantes = 'qwrtypsdfghjklçzxcvbnm'
    while indice < len(frase):
        frase = frase.replace(consoantes[indice], consoantes[indice].upper())
        indice += 1
    return frase