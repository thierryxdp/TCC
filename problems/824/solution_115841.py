def uppCons(frase):
    x = ""
    contador = 0
    vogais = "aeiouAEIOU"
    while contador < len(frase):
        if frase[contador] not in vogais:
            nova_frase = x + frase[contador].upper()
        else:
            nova_frase = x + frase[contador]
        contador = contador + 1
    return nova_frase