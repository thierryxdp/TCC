def colchao(A,B,C,H,L):
    '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    A=espessura do colchão
    B=largura do colchão
    C=comprimento do colchão
    H=altura da porta
    L=largura da porta
    float,float,float ->str'''
    if A<L and B<H:
        return True
    if B<H and A<L:
        return True
    if C<H and B<L:
        return True
    elif:
        return False