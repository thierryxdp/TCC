def soma_h(n):
    """Função que calcula o valor de hm com n termos.
        int->float"""
    soma=0
    for i in range(1,n+1):
        soma=soma+1/i
    
    return round(soma,2)