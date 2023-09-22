def qtd_divisores(n):
    """função que dado um número inteiro ela calcula e retorna quantos
    divisores este número possui
    exemplo: 10 tem 4 divisores(1,2,5,10)
    
    entrada-> int
    retorna-> int"""
    divisores=0
    
    for i in range(1,n+1):
        if n%i==0:
            divisores= divisores+1
            
    return divisores