def colchao(medidas,H,L):
    medidas = [A,B,C]
    medidas[0]=A
    medidas[1]=B
    medidas[2]=C
    if (H*L) < (medidas[0]*medidas[1]):
        return "False"
    if (H*L) >= (medidas[0]*medidas[1]):
        return "True"