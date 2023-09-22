def total(lista,prd):
    som = 0
    for k,v in prd.items(lista):
        som += v
    return round(som,2)