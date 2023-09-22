def uppCons(frase):
    lista = ["a","e","i","o","u"]
    for x in lista:
        if x not in frase:
            frase[x] = str.upper(x)
            
    return frase