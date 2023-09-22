def total (compras , preco):
    '''dada uma lista de compras com os nomes dos produtos e um dicionário
    com os produtos da loja e seus preços, retorna o valor total da lista
    de compras
    list,dict -> float'''
    
    soma_preco = 0
    
    for produto in compras:
        if produto in preco:
            soma_preco += dict.get (preco, produto)
    return round(soma_preco,2)