def total(compras, produtos):
    '''Dada uma lista de compras e um dicionário com os nomes
    e preços dos produtos de uma loja, retorna o valor dos 
    produtos na lista somados.
    list , dict -> float'''
    
    acumul = 0
    for item in produtos:
        if item in compras:
            acumul += produtos[item]
    return acumul