def total(compras,mercado):
    '''
    '''
    
    final=0
    
    for elementos in compras:
        if compras in mercado:
            final=final+mercado[compras]
            round(final,2)
            
    return final