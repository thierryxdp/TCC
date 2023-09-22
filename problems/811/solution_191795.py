def colchao(medidas, H, L):
    A = int(medidas[0])
    B = int(medidas[1])
    C = int(medidas[2])
    return ((A*B) <= (H*L)) or ((B*C) <= (H*L)) or ((A*C) <= (H*L))