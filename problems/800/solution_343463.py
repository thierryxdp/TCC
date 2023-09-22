def total(lista_compras,preco_produto):
    '''
       Dada uma lista de compras e um dicionário com os 
       preço dos produtos a função retorna a soma dos valores
       dos produtos que estão na lista de compras.
       list, dict -> float
    '''
    total=0
    for produto in lista_compras:
        total = total + dict.values(preco_produto)
    return round(total, 2)