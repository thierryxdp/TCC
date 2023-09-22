def qtd_divisores(n):
    div = 1
    
    for i in range (2,n+1):
        if n % div == 0:
            div+=1
            
    return div