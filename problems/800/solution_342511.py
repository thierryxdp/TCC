def total(lista, dicionario):
    list = []
    for i in dicionario:
        if i == lista:
            list.append(dicionario[i])
    soma = sum(list)
    return round(soma, 2)