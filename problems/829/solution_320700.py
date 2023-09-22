soma_h(N):
    """Esta funcao calcula e retorna o valor de H com N termos, onde N
    é dado como parametro."""
    soma = 0
    for c in range(1,n+1):
        inverso = (1/c)
        soma += inverso
    return round(soma,2)