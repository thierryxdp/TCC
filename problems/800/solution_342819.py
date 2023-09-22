def total(compras,mercado):
    '''
    '''
    
    final=0
    i=0
    for elementos in compras:
        if compras[i] in mercado:
            final=final+mercado[compras[i]]
            
            
    return round(final,2)