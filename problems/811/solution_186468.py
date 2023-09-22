def colchao(medidas,H,L):
    '''função que verifica se é possivel as 'medidas' de determinado colchao passar pelas portas de altura H largura e altura L'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if A>B and A>C:
        return (B<=H and C<=L) or (C<=H and B<=L)
    if B>A and B>C:
        return (A<=H and C<=L) or (C<=H and A<=L)
    if C>B and C>A:
        return (B<=H and A<=L) or (A<=H and B<=L)