def total(lista, dic):
    #recebe uma lista de compras e um dicionário de produtos e retorna o valor total que será gasto
    total = 0
    for i in lista:
        if i in dic:
            total += dic[i]
    return total