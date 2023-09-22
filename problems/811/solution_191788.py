def colchao(medidas,H,L):
    '''calcula medidas do colchao necessárias para passar por portas
    list(int,int,int)->bool'''
    
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if min(B,C)<H or min(B,C)<L:
        return True
    else:
        return False