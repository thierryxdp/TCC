def maiores(lista,num):
    add = lista.append(num)
    list(filter(maiores,lista))
    return add