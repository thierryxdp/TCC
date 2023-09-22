def colchao(medidas,H,L):
    """função que dadas as medidas do colchão e da porta, retornam true caso passe e false caso o colchão não passe; int,int,int,int,int-->string"""
    medidas= A,B,C
    porta= H,L
    if medidas[1]>porta[0] and medidas[1]>porta[1]:
        return True
    else:
        return False