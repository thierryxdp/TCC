def total(lista,produtos):
    """retorna o valor total dos itens da lista que estejam
    disponiveis na loja, dado uma lista de compras e um dicionario
   que contem o preco de cada produto disponivel na loja.
   list, dict -> float"""
    l1 = list(produtos)
    preco = 0
    for produto in lista:
        if produto in l1:
            preco = preco + produtos[l1[list.index(l1,produto)]]
    return round(preco,2)