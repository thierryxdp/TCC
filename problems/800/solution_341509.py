def total(lista,produtos):
    '''Recebe uma lista de compras e um dicionario contendo o preco de cada produto e retorna
    o valor total dos itens que estejam disponíveis nesta loja.
    list,dict-> float'''
    total=0
    for elem in lista:
        if elem in produtos:
            total=total+produtos[elem]
    return round(total,2)