def uppCons(frase):
    frase3 = ""
    contador=0
    while contador<len(frase):
        letra = frase[contador]
        if letra.lower() not in "aáãâeéêiíîoóôõuúû":
            frase3 += letra.upper()
        else:
            frase3 += letra
        contador += 1
    return frase3