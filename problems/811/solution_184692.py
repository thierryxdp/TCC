def colchao(medidas,H,L):
    """define se um colchão passa por uma porta;lista,int,int->bool"""
    largura_colchao=[medidas[1]]
    comprimento_colchao=[medidas[2]]
    altura_porta=[H]
    largura_porta=[L]
    if largura_colchao>altura_porta and comprimento_colchao>largura_porta:
        return 2==3
    else:
        if largura_colchao<altura_porta and comprimento_colchao<largura_porta:
        return 2==2