def total(lista_compras,preco_produto):
    '''
       Dada uma lista de compras e um dicionário com os 
       preço dos produtos a função retorna a soma dos valores
       dos produtos que estão na lista de compras.
       list, dict -> float
    '''
    total=0
    for i in dict.values(preco_produto):
        if lista_compras in dict.keys(preco_produto):
            total = total + preco_produto[key in lista_compras]
    return round(total, 2)