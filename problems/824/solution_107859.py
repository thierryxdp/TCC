def uppCons(frase):
    """ """
    lista1 = []
    for i in frase:
        if (i in "AEIOUaeiou"):
            lista1.append(i)
        else:
            lista1.append(upper(i))
    return lista1