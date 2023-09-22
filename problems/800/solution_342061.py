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
    lista1 = list(produto)
    preco = 0
    for produto in lista1:
        if produto in lista1:
            preco = preco + produtos[lista1[list.index(lista1,produto)]]
    return round(preco,2)