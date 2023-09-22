def total(compras,valor):
    total=0
    j=0
    for j in range(0,len(compras)):
        if compras[j]in valor.keys():
            total=valor[compras[j]]+total
    return round(total,2)