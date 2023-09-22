def soma_h(N):
    """Funcao que dado como parametro de entrada um inteiro
    N, calcula e retorna o valor de H=(1+(1/2)+(1/3)+...
    +(1/N)) com N termos;
    int->float"""
    
    Soma=0
    
    for denominador in range(1,N+1):
        Fracao=(1/denominador)
        Soma=Soma+Fracao
    return round(Soma,2)