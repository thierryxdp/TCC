def fatorial(n):
    """ Função que, dados uma"""
  
    ct1 = 1
    ct2 = 0
    
    while ct1 < n:
        var = n*(ct1)
        ct1 = ct1 + 1
        var = var + var*ct2
        ct2 = ct2 + 1     
    
    return var