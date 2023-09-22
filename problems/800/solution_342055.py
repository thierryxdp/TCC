def total (compras, preco_produtos):
    ''' Entrada: compras -> lista de compras, dado do tipo
    						list
                 preco_produtos -> dicionario contendo o 
                 				   o preço de cada produto
                                   disponível em determinada
                                   loja, dado do tipo dict
        
        Saída: Total -> dado do tipo float igual ao valor 
        				total dos itens da lista que estejam
                        disponíveis na loja
        
        list,dict -> float'''
    l1 = list(produtos)
    preco = 0
    for produto in lista:
        if produto in l1:
            preco = preco + produtos[l1[list.index(l1,produto)]]
    return round(preco,2)