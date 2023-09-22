def total(lista_compras,precos):
    i=0
    valor=0
    while i<len(lista_compras):
        valor=valor + dict.get(precos,lista_compras[i])
        i=i+1
    return round(valor,2)