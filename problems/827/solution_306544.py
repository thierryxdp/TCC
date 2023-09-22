def qtd_divisores(n):
   
    
    quantidade = filter(lambda x: n%x == 0,range(1,n+1))
    return quantidade