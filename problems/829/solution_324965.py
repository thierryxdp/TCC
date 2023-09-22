def soma_h(n):
    """Função que recebe um inteiro
    e calcula a série harmônica de N.
    int -> float"""
    soma = 0
    for x in range(1, n+1):
        soma += 1/x
    return round(soma, 2)