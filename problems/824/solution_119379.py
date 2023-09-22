def uppCons(frase):
    lista = ["a","e","i","o","u"]
    for x in lista:
        if x in frase:
            frase = str.upper(frase)
    return frase