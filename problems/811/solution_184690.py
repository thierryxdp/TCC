def colchao(medidas,H,L):
    """define se um colchão passa por uma port;list,int,int->bool"""
    largura_colchao=[medidas[1]]
    comprimento_colchao=[medidas[2]]
    if largura_colchao>H and comprimento_colchao>L:
        return 2==3