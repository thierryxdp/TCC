def colchao(medidas,H,L):
    if int(medidas[0])*int(medidas[1]) <= (H*L):
        return "True"
    else:
        return "False"
    if int(medidas[1])*int(medidas[2]) <= (H*L):
        return "True"
    else:
        return "False"