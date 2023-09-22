def colchao(medidas,H,L):
    A, B, C = medidas
    return H >= A and L >= B or H >= B and L >= A