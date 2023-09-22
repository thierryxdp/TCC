def total (lista,precos):
    lst = []
    for i in lista:
        lst.append(precos[i])

    return round(sum(lst),2)