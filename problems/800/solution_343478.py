def total(lista_compras,produtos):
    '''
       Dada uma lista de compras e um dicionário com os 
       preço dos produtos a função retorna a soma dos valores
       dos produtos que estão na lista de compras.
       list, dict -> float
    '''
    total=0
    for lista_compras in dict.keys(produtos):
        if lista_compras == dict.keys(produtos):
        total = sum(dict.values(produtos))
    return total