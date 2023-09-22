def uppCons(frase):
    vogais = ['A','E','I','O','U','a','e','i','o','u','ã','á','é','í','ó','ú']
    indice = 0
    frase = list(frase)
    for letra in frase:
        if frase[indice] not in vogais:
            frase[indice] = frase[indice].upper() 
        indice += 1
    return "".join(frase)