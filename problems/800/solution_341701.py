def total(lista_compras,dicio_precos):
    '''
    	Função que recebe uma lista 
        de compras e um dicionário
        com os preços dos produtos
        disponíveis em uma loja, e
        retorna o preço total dos 
        itens da lista que estejam
        disponíveis nessa loja
        : param lista_compras: list
        : param dicio_precos: dict
        : return: float
    '''
    preco_total = 0
    
    for produto in lista_compras:
        if produto in dicio_precos:
            preco_total += dict.get(dicio_precos,produto)
    
    return round(preco_total,2)