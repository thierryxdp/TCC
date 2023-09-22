def carros(n, cap = 5):

    q = n / cap
    
    resto = n % cap
    
    if resto >= 1 and resto < (cap/2):
        
        return int(round(q) + 1)
   
    elif resto >= (cap/2):
        
        return int(round(q))
    
    else:
        return int(q)