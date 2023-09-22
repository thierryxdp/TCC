def uppCons(frase):
    contador = 0
    while contador<len(frase):
        if frase[contador]=='a':
            frase[contador] = "A"
        contador = contador + 1
    return frase