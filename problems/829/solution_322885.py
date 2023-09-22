def soma_h(N):
    '''dado um numero N nteiro, podemos por essa funçao
    calcular o somatorio de 1^(-1)+2^(-1)+3^(-1)+........+
    (N-2)^(-1)+(N-1)^(-1)+N^(-1); e esse valor arredondado
    em 2 casas decimais
    int-->float'''
    
    soma=0
    for i in range(N):
        if N!=0:
            soma=soma+(1/(i+1))
    return round(soma,2)