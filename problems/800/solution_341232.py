def total(lista,produtos):
    ''''''
    l1 = []
    for i in produtos:
        l1 = l1 + [produtos[i]]
    return round(sum(l1))