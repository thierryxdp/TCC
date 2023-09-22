def total(lista_compras,produto):
    """ Funçao que retorna o valor total dos itens da lista dada que
    estejam disponiveis em uma loja"""
    
    
    lista_compras = []
    produto = dict.items(produto)
    itens = 0
    
    for i in len(lista_compras):
        if produto in lista_compras[i]:
            lista_compras = lista_compras + produto
            
            return round(produto,2)