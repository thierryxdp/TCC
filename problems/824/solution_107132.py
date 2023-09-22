def uppCons(frase):
    indice=0
    while indice < len(frase):
        if frase[indice] not in "AEIOUaeiou":
            frase=str.upper(frase[indice])
        indice=indice+1
    return frase