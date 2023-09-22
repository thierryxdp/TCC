def total(lista,produtos):
    compras=[]
    
    for prod in lista:
        if produtos in lista:
            compras=compras + [prod]
    return round(compras,2)