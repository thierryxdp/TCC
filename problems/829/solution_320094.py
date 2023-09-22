def soma_h(N):
    """dado um número inteiro N, a função calcula e retorna o valor H da soma de todos os inversos de 1 até N, isto é, 
    retorna o valor H = 1 + 1/2 + ... + 1/N (com duas casas decimais); int -> float"""
    soma = 0
    for i range(1, N+1):
        soma += 1/i
    return round(soma,2)