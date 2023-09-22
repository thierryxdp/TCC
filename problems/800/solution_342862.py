def total(compra,preco):
    
    i = 0
    gasto = 0
    while i < len(compra):
         if compra[i] in preco:
            custo = dict.get(preco,compra[i])
            gasto = gasto + custo
        
    return round(gasto,2)