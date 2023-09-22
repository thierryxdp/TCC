def uppCons(frase):
    indice=0
    while indice <len(frase):
        if frase[indice] != 'a','e','i','o','u':
            frase[indice] = str.upper(frase[indice])
        indice= indice+1
    return frase