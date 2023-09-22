def colchao(A,B,C,H,L):
    medidas = [A,B,C]
    if int(A)*int(B) <= (H*L):
        return "True"
    else:
        return "False"
    if int(B)*int(C) <= (H*L):
        return "True"
    else:
        return "False"