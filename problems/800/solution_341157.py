def total(lista,produtos):
    compras=[]
    
    for prod in lista:
        if produtos in lista[prod]:
            compras=conoras + [prod]
    return compras