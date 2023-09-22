def colchao(medidas,H,L):
    
    A,B,C = medidas
    medidas = A*B*C
    
    if A and B < max(H,L):
        return True
        
    if A and C < max(H,L):
        return True
    
    if B and C < max(H,L):
        return True
  
    else:
        return False