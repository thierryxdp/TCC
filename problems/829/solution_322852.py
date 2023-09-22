def soma_h(N):
    """
    Calcula e retorna o resultado da sequência 1+1/N;
    int -> float
    """
    soma = 0
    for i in range(i,N+1):
    	soma = soma + 1/i
    return round(soma,2)