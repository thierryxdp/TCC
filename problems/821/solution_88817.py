def fatorial(n):
    """ Função que, dados uma"""
  
    ct1 = 1
    ct2 = 0
    
    while ct2 < n:
        ct1 = ct1*(n-ct2)
        ct2 = ct2 + 1     
    
    return ct1