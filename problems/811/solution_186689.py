def colchao(medidas,H,L):
    ''''''
    [A,B,C] = medidas
    
    if (H < A or H < B or H < C) :
        return False
    if (H > A or H > B or H > C):
        return True