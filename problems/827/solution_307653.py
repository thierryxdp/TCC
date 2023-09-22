def qtd_divisores(n):
    """conta quantos divisores tem um numero n
    int-->int"""
    divisores=[]    
    for var in range(1,n+1):
        if n%var==0:
            list.insert(divisores,0,var)
    return len(divisores)