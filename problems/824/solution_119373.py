def uppCons(frase):
    lista = ["a","e","i","o","u"]
    for x in lista:
        if x in frase:
            frase = frase
        else:
            frase[x]=str.upper(x)
    return frase