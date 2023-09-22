def total(compras,mercado):
    '''
    '''
    Scompras=compras.split()
    final=[]
    
    for elementos in range(len(compras)):
        if Scompras in mercado:
            final=final+mercado[Scompras]
           
            
    return round(final,2)