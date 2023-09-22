def colchao(medidas,H,L):
    """retorna True se o colchao passa pelas portas e falso se nao. list,int,int->Bool"""
    return (medidas[0]<=L and medidas[1]<=H)or(medidas[0]<=H and medidas[1]<=L)