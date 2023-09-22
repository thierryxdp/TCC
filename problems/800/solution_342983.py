def total(x,y):
    """ """
    proximo = 0
    contador = 0
    for x in y:
        if x in y[proximo]:
            proximo = proximo + 1
            contador = contador + codict.get(y,proximo)
     return contador