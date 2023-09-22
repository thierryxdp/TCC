def colchao(medidas,H,L):
    ''''''
    [A,B,C] = medidas
    
    if (H > C or B > H or L > B or C > L):
        return False
    else:
        return True