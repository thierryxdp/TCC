def total(lista, produtos):
    'retorna o valor do itens contidos na lista list,dict -> int'
    i = 0
    j = 0
    while i < len(lista):
        if lista[i] in produtos:
            j += produtos[lista[i]]
        i += 1
    return round(j,2)