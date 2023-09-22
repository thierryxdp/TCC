def faltante(n):
    m = 0
    n2 = n[:]
    while m<len(n2):
        if n[m] != m+1 :
            resp1 = m+1
            return resp1
        else: 
            m = m + 1
            
    
    resp2 = m+1
    return resp2