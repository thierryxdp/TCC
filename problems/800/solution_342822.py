def total(compras,mercado):
    '''
    '''
    
    final=0
    i=0
    for elementos in range(len(compras)):
        if compras in mercado:
            final=final+mercado[compras]
           
            
    return round(final,2)