def qtd_divisores(n):
    p= list(range(1,n+1))
    soma = 0
    for x in range(1,n+1):
        if n%x==0:
            soma = soma + ((n+1)-n)
            
            
    return soma