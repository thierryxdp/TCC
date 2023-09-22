def colchao(medidas,H,L):
    A = int(medidas[0])
    B = int(medidas[1])
    C = int(medidas[2])
    if (H + L) > (A*0 + B + C): return "True"
    if (H + L) <= (A*0 + B + C): return "False"