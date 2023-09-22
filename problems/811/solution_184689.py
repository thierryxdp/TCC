def colchao(medidas,H,L):
    """define se um colchão passa por uma port;list,int,int->bool"""
    largura_colchao=[medida[1]]
    comprimento_colchao=[medida[2]]
    if largura_colchao>H and comprimento_colchao>L:
        return 2==3