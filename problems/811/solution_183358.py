def colchao(A,B,C,H,L):
    """dadas as dimensões do colchão e da porta, a função retorna True
    se o colchão consegue passar pela porta e False se ele não consegue.
    int, int, int, int, int-->bool
    
    Parâmetros
    A: menor dimensão do colchão
    B: segunda menor dimensão do colchão
    C: maior dimensão do colchão
    H: altura da porta
    L: largura da porta"""
    if A<H and B<L:
        return True
    else:
        if B<H and A<L:
            return True
        else:
            return False