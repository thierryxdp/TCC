def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if ((H>A)and(L>B))or((H>B)and(L>A)):
        return True
    elif((H>A)and(L>C))or((H>C)and(L>A)):
        return True
    elif((H>B)and(L>C))or((H>C)and(L>B)):
        return True
    else:
        return False