def fatorial(n):
    """
    Função que recebe um número inteiro e retorna seu fatorial
    
    int ---> int
    
    *versão usando for
    """
    fatorial=1
    
    for i in range(1,n+1):
        fatorial*=i
    return fatorial