def colchao(medidas,H,L):
    menor_dim = min(medidas[0],min(medidas[1:]))
    menor2_dim = min(max(medidas[:2],min(max(medidas[0],medidas[1]),max(medidas[1],medidas[2]))))
    if menor_dim <= L and menor2_dim <= H:
        return True
    else:
        return False