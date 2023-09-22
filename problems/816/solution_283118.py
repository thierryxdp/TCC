def maiores([lista],n):
    lista_nova = [lista] + [n]
    list.sort(lista_nova)
    return lista_nova