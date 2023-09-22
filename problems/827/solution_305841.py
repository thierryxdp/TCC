def qtd_divisores(n):
    divisores=[]    
    for var in range(n+1):
        if n%var==0:
            list.insert(divisores,0,var)
    return len(divisores)