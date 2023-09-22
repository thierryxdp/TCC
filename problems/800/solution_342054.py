def compras(compras,mercado):
    """lel"""

    i = 0
    
    if compras[0] in mercado:
        i = i+mercado[compras[0]]
    if compras[1] in mercado:
        i = i+mercado[compras[1]]
    if compras[2] in mercado:
        i = i+mercado[compras[2]]
    return i