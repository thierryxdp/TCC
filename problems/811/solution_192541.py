def colchao(medidas,H,L):
    return (medidas[0]<=L and medidas[1]<=H)or(medidas[0]<=H and medidas[1]<=L)