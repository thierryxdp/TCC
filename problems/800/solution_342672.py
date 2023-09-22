def total(lista,dici):
    'descrição'
    li = []
    for i in lista:
        if i in dici:
            li += [dici[i]]
    return li