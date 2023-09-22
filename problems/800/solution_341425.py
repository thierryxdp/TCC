def total(compras,produtos):
    total=0
    for i in compras:
        total+=produtos[i]
    return round(total,2)