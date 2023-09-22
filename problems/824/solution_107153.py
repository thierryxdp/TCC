def uppCons(frase):
    indice=0
    while indice < len(frase):
        if frase[indice] not in "AEIOUaeiou":
            frase=frase[:indice]+str.upper(frase[indice])+frase[indice+1:]
        indice=indice+1
    return frase