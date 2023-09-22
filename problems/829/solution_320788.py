def soma_h(N):
    """Esta função recebe um número inteiro e calcula a soma dos inversos de um até este número retornando o valor com 2 casas decimais
    int -> float"""
    H = 0
    for i in range(1,N+1):
        H += 1/i
    return round(H,2)