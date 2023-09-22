def total (listaCompras, precoP):
    '''Dada uma lista de compras e um dicionário com os 
       preços dos produtos, retorne o valor total dos itens 
       da lista que estejam disponíveis na loja;
       list, dict -> float'''
    total = 0
    for itens in listaCompras:
        if in precoP.keys():
            total = total + precoP[itens]
    return round(total,2)