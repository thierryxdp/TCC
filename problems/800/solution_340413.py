def total(lista_compras,preco_produtos):
    '''Função que, dada uma lista de compras e o preço de produtos, retorna o valor total dos itens a serem comprados.
list,dict --> float'''
    lista_preco = list(preco_produtos)
    preco = 0
    for produto in lista_compras:
        if produto in lista_preco:
            preco = preco + preco_produtos[lista_preco[list.index(lista_preco,produto)]]
    return preco