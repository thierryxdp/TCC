def uppCons(frase):
    vogais = ['A','E','I','O','U','a','e','i','o','u']
    indice = 0
    for letra in frase:
        if frase[indice] in vogais:
            frase[indice].upper() 
        indice += 1
    return frase