def total(compras, preco_prod):
    
    val_total = 0
    
    for prod in compras:
        
        if prod in preco_prod:
            
            val_total += preco_prod[prod]
    
    return round(val_total,2)