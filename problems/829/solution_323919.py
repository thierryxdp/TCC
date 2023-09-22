def soma_h(num):
    """Função recebe um inteiro e calcula a série harmônica de N."""
    soma = 0
    for x in range(1, num+1):
        soma += 1/x
    return round(soma, 2)