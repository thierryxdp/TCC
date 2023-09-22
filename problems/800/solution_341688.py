def total(compras,produtos):
    """
    
    """
    total=0
    for i in range(len(compras)):
        if compras[i] in produtos:
            total+=produtos[compras[i]]
    return round(total,2)