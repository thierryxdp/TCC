def primo(n):
    """dado um número inteiro positivo a função calcula se é primo ou não
    entrada->int
    retorna->bool"""
    
    primos=0
    
    for i in range(2,n):
        if n%i==0:
            primos= primos+1
            
    return  primos==0