def soma_h(N):
    """A função recebe um numero N, que é inteiro e positivo, e retorna
    a soma do fatorial de N elevado a -1;
    int -> float"""
    soma = 0
    for i in range(1,N+1):
        soma += i**-1
    return round(soma,2)