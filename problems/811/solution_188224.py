def colchao(A,B,C,H,L):
    '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    A=espessura do colchão
    B=largura do colchão
    C=comprimento do colchão
    H=altura da porta
    L=largura da porta
    float,float,float ->str'''
    if A<L or B<H:
        return True
    if B<H or A<L:
        return True
    if C<H or B<L:
        return True
    if A>L or B>H:
        return False
    if B>H or A>L:
        return False
    if C>H or B>L:
        return False