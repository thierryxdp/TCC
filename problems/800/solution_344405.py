def total(lista,prods):
    i=0
    valor=0
    while i < len(lista):
        valor = valor + prods(lista[i])
        i=i+1
    return round(valor,2)