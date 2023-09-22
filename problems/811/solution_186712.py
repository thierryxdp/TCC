def colchao(medidas,H,L):
    medidas = ['A','B','C']
    if (H*L) < (medidas[0]*medidas[1]):
        return "False"
    if (H*L) >= (medidas[0]*medidas[1]):
        return "True"