def soma_h(N):
    """funcao que calcula e retorna o somatorio de 1/(N), em
    que N e um numero inteiro positivo dado de entrada;
    int -> float"""
    
    soma = 0
    for i in range(1,N+1):
        soma = soma + (1/i)
    return round(soma,2)