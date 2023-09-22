def total(lista,dicio):
    valor=0
    for i in lista:
        if i in dicio:
            valor+= dicio[i]
    return round(valor,2)