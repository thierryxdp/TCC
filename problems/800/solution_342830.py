def total(compras,mercado):
    '''
    '''
    
    final=0
    
    for i in range(len(compras)):
        if compras in mercado:
            final=final+mercado[compras]
           
            
    return round(final,2)