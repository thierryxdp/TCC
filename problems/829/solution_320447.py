def soma_h(n):
    """
    Função que calcula a soma da sequencia
    1/1+1/2+1/3+...+1/n com uma precisão de 
    duas casas decimais.
    
    int -- > float
    """
    soma=0
    for i in range(1,n+1):
        termo=1/i
        soma+=termo
    return soma