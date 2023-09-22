def colchao(medidas,H,L):
    
    A,B,C = medidas
    medidas = A*B*C
    
    if A,B < max(H,L):
        return True
        
    if A,C < max(H,L):
        return True
    
    if B,C < max(H,L):
        return True
  
    else:
        return False