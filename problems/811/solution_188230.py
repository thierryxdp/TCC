def colchao(medidas,H,L):
    '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    A=espessura do colchão
    B=largura do colchão
    C=comprimento do colchão
    H=altura da porta
    L=largura da porta
    float,float,float ->str'''
    medidas=A,B,C
    A<B<C
    H>L
    if C<H or B<L:
        return True