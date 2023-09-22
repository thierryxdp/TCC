def colchao(medidas,H,L):
    '''função que, dada uma lista com as dimensões do colchão, a altura da porta H e a largura da porta L, retorna True se o colchão passar pela porta e False se não passar.
    entrada: lista, int, int
    saída: bool'''
    
    B=medidas[1]
    C=medidas[2]
   
    
    if (B<H and C>L) or (B==H and C>L):
        return True
    else:
        return False