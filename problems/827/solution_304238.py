def qtd_divisores(n):
    div = 0
    
    for i in range (2,n):
        if n % div == 0:
            div+=1
            
    return div