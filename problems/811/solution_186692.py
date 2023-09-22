def colchao(medidas,H,L):
    ''''''
    [A,B,C] = medidas
    
    if (H > A or H > B):
        return True
    if (C > H or C > L):
        return True
    else:
        return False