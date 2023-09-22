def colchao(medidas,H,L):
    '''Função que verifica se é possível ou não de passar o
    colchão pela porta da casa.
    float,float,float ->str'''
    medidas=A,B,C
    A=espessura do colchao
    B=largura do colchao
    C=comprimento do colchao
    H=altura da porta
    L=largura da porta
    A<B<C
    H>L
    if C<H or B<L:
        return True