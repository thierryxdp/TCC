def uppCons(frase):
    frase2=list(frase)
    frase3 = ""
    contador=0
    while contador<len(frase2):
        letra = frase2[contador]
        if letra.lower() not in "aeiou":
            frase3 += letra.upper()
        else:
            frase3 += letra
        contador += 1
    return frase3