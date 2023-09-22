def total(lista,dici):
    'descrição'
    cont = 0
    for i in lista:
        if i in dici:
            cont += dici[i]
        return cont