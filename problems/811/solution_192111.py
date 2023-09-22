def colchao(medidas,H,L):
    A, B, C = medidas
    return H >= B and L >= C or H >= C and L >= B