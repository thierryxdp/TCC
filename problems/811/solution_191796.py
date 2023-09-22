def colchao(medidas, H, L):
    A = int(medidas[0])
    B = int(medidas[1])
    C = int(medidas[2])
    return: (((A <= H) and ((B or C) <= L)) or (((B <= H) and ((A or C) <= L)) or (((C <= H) and ((B or A) <= L))