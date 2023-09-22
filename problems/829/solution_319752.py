def soma_h(N):
    """Função que calcula e retorna o valor de H com N termos
    int -> float"""
    soma = 0
    for numero in range(1, N+1):
        soma += 1/numero
    return round(soma, 2)