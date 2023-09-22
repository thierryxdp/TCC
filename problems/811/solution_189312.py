def colchao(medidas,H,L):
    
    if medidas[1] <= H and medidas[0] <= L:
        passar = True
    
    if medidas[1] <= L and medidas[0] <= H:
        passar = True
    
    else:
        passar = False
    
        
    return passar