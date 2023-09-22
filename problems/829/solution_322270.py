def soma_h(N):
    """retorna com 2 casas decimai o valor de H com N termos, onde N de entrada
    int -> float"""
    soma = 0
    for x in range(1,N+1):
        soma = soma + 1/x
    return round(soma,2)