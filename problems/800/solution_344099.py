def total(lista, dici):
    valor = 0
    for i in range(len(lista)):
        if lista[i] in dici:
            valor += dici[lista[i]]
    return round(valor, 2)