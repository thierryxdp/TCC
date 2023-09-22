def uppCons(frase):
    
    contador = 0
    vogais = "aeiouAEIOU"
    while contador < len(frase):
        if frase[contador] not in vogais:
            frase[contador].upper()
        contador = contador + 1
    return frase