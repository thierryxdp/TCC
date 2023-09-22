def qtd_divisores(n):
    """
    Função que calcula a quantidade de divisores inteiros
    de um número n
    
    int -- > int
    """
    
    div=0
    for i in range(1,(n//2)+2):
        if n%i==0:
            div+=1
    return div