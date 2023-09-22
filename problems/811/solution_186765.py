def colchao((A,B,C),H,L):
    medidas = [A,B,C]
    if (H*L) < int(medidas[0])*int(medidas[1]):
        return "False"
    if (H*L) >= int(medidas[0])*int(medidas[1]):
        return "True"