def total(produtos,prd):
    som = 0
    for k,v in produtos.items():
        som += v
    return round(som,2)