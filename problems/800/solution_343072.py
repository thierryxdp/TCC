def total(produtos, preços):
    '''função que passa um dicionário com o valor total de uma compra''' 
    total = 0
    for item in produtos:
        if item in preços:
            total = total + preços[item]
    return round(total, 2)