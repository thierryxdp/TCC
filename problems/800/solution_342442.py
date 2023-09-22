def total (lista,precos):
    lst = []
    for i in lista:
        lst.append(precos[i])

    return sum(lst)