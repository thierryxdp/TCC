def uppCons(frase):
    vogais = ['A','E','I','O','U','a','e','i','o','u']
    indice = 0
    frase = list(frase)
    for letra in frase:
        if frase[indice] not in vogais:
            print (frase[indice])
            frase[indice] = frase[indice].upper() 
        indice += 1
    return "".join(frase)