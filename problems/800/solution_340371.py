def total(compras,produtos):
    '''Função que retorna o valor final da compra de 
    uma pessoa; recebe a lista de compra da pessoa e 
    o valor dos produtos de um mercado; List,Dict-->Float'''
    valor_compras=0
    for produto in compras:
        valor_compras+=dict.get(produtos,produto,0)
    return round(valor_compras,2)