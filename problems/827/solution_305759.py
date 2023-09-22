def qtd_divisores(n):
    """Funcao que dado como parametro de entrada um numero
    n, conta e retorna quantos divisores esse numero possui;
    int->int"""
    
    Quantidade=0
    
    for divisor in range(1,n+1):
        if n%divisor==0:
            Quantidade=Quantidade+1
    return Quantidade