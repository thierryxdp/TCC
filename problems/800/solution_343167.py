def total(compras, precos):
    i = 0
    total_gasto= 0
    while i < len(compras):
         if compras[i] in precos:
            custos = dict.get(precos,compras[i])
            total_gasto = total_gasto + custos
            i += 1
        
    return round(total_gasto,)