def colchao(medidas,H,L):
    '''função que verifica se é possivel as 'medidas' de determinado colchao passar pelas portas de altura H largura e altura L'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if A>B and A>C:
        return A<=H and (B>=L or C>=L)
    if B>A and B>C:
        return B<=H and (A>=L or C>=L)
    if C>B and C>A:
        return C<=H and (B>=L or C>=L)