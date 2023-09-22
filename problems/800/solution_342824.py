def total(compras,mercado):
    '''
    '''
    
    final=[]
    
    for elementos in range(len(compras)):
        if compras in mercado:
            final=final+mercado[compras]
           
            
    return round(final,2)