def colchao(medidas,H,L):
    '''função que, dada uma lista com as dimensões do colchão, a altura da porta H e a largura da porta L, retorna True se o colchão passar pela porta e False se não passar.
    entrada: lista, int, int
    saída: bool'''
    medidas=A,B,C
    
    if B<=H and L<=C :
        return True
    if B>H or L>C :
        return False