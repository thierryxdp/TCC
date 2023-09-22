def fatorial(n):
    """
    Função que recebe um número inteiro e retorna seu fatorial
    
    int ---> int
    
    *versão usando recursividade
    """
    if n==1:
        return 1
    else:
        return n * fatorial(n-1)