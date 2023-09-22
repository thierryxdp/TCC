def qtd_divisores(n):
    
    i=0
    for x in range(n+1):
        if 10%(x+1)==0:
            i=i+1
    return i