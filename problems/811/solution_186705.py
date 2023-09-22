def colchao(medidas,H,L):
    ''''''
    [A,B,C] = medidas
    
    if (H > A or H > B or C > H or C > L):
        return True
    else:
        return False