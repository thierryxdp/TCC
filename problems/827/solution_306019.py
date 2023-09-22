def qtd_divisores(n):
    """Dado um número retorna o total de divisores que 
    este números possui;
    int -> int"""
    a = list(range(1,n+1))
    resultado = [] 
    for x in a : 
        if x%n==0 :
            list.append(resultado,x)
    
    return len(resultado)