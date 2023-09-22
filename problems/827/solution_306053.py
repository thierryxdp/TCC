def qtd_divisores(n):
    
    """
    Função que retorna a quantidade de divisores
    que o número dado como paramêtro de entrada tem.
    int-->int
    """
    qtd_divisores=0
    for i in range(1,n+1):
        if n%i==0:
            qtd_divisores+=1
    return qtd_divisores