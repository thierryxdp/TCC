def carros(n, cap = 5)

	q = n / cap
    
    resto = n % cap
    
    if resto >= 1 and < 5:
        
        return round(q) + 1
    elif resto >= 5:
        return round(q)