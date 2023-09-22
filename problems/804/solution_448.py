filtra_pares (a, b, c, d):
    """>"""
    a = a / 2
    b = b / 2
    c = c / 2
    d = d / 2
    
    if (a == 0):
        return (a)
    
    elif (b == 0):
        return (b)
    
    elif (c == 0):
        return (c)
    
    elif (a and b == 0):
        return str (a, b)
    
    elif (a and c == 0):
        return str (a, c)
    
    elif (a and d):
        return (a, d)
    
    elif (b and c == 0):
        return str (b, c)
    
    elif (b and d == 0):
        return (b, d)
    
    elif (c and d == 0):
        return str (c, d)
    
    elif (a and b and c):
        return (a, b, c)
    
    else: 
        return (a, b, c, d)