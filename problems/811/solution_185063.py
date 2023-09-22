def colchao(medidas,H,L):
    """função que dadas as medidas do colchão e da porta, retornam true caso passe e false caso o colchão não passe; int,int,int,int,int-->string"""
    if medidas[1]>H and medidas[1]>L:
        return True
    else:
        return False