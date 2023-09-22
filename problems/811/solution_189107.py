def colchao(medidas,H,L):
    '''função que, dada uma lista com as dimensões do colchão, e dado H a 
    altura da porta e L a largura da porta, retorna True se o colchão
    passar pela porta e False se não passar.
    entrada: lista, int, int
    saída: bool'''
    
    B=medidas[1]
    C=medidas[2]
   
    
    if (B<H and C>L) or (B==H and C>L) or (B>H and C<L) or (B<H and C<L):
        return True
    else:
        return False