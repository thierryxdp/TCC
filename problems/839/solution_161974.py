def carros (c,p): 
    if c = p:
        x = p/c
    elif c = 5 and p % 5 =0:
        x = p//c 
    elif c = 5 and p % 5 != 0:
        x = p//c + 1
    elif p = 0 or c = 0: 
        x = 0
    elif p < c: 
        x = 1 

    else: 
        x = p/c 
    return x