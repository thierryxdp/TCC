soma_h(N):
    """Esta funcao calcula e retorna o valor de H com N termos, onde N
    é dado como parametro."""
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)