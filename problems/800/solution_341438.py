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
    
    total = 0
    for produto in preco_produtos:
        if compras in preco_produtos[produto]:
            total= total+[produto]
    return total