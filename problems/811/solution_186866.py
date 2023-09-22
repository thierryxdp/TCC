def colchao(medidas,H,L):
    return (medidas[0]<=H and medida[1]<=L) or\
    (medidas[1]<=H and medida[0]<=L) or\
    (medidas[0]<=H and medida[2]<=L) or\
    (medidas[2]<=H and medida[0]<=L) or\
    (medidas[1]<=H and medida[2]<=L) or\
    (medidas[2]<=H and medida[1]<=L)