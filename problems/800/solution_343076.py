def total(produtos, precos):
    '''função que passa um dicionário com o valor total de uma compra''' 
    total = 0
    for item in produtos:
        if item in precos:
            total = total + precos[item]
    return round(total, 2)