def uppCos(frase):
    indice=0
    UC=""
    while indice <= (len(frase)-1):
        if frase[indice] not in "AEIOUaeiou":
            UC=UC + frase[indice]
        indice = indice + 1
        return UC.upper()