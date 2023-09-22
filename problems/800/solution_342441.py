def total (lista,preços):
    lst = []
    for i in lista:
        lst.append(preços[i])

    return sum(lst)