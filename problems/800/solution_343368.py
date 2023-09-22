def total(compras,valor):
    soma=0
    j=0
    for j in range(0,len(compras)):
        if compras[j]in valor.keys():
            total=valor[compras[j]]+soma
    return round(soma,2)