def total(compras,mercado):
    '''
    '''
    
    final=0
    
    for i in range(len(compras)):
        if compras[i] in mercado:
            final=final+mercado[compras[i]]
           
            
    return round(final,2)