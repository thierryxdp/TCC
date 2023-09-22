def colchao(medidas,H,L):
    '''calcula medidas do colchao necessárias para passar por portas
    list(int,int,int)->bool'''
    
    medidas=[A,B,C]
    
    if min(A,B,C)<H or min(A,B,C)<L:
        return True
    else:
        return False