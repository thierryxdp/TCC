def total(compras,d):
    
    valor = 0
    
    for item in compras:

        valor = valor+d[item]
    
    return valor