def bolos(a, b, c):
    
    x = a//2
    o = b//3
    l = c//5
    
    if x<=o ^ x<=l:
        return x 
    elif o<=x ^ o<=l:
        return o
    else:
        return l