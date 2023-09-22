def total(lista, dicionario):
    total = []
    for produto in dicionario:
        if produto in lista:
            a = dict.get(dicionario, produto)
            list.append(total, a)
    b = sum(total)
    return b