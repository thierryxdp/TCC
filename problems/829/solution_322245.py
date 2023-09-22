def soma_h(n):
    """ Função que dados um número inteiro retorna a soma da média
    harmônica
    int -> float"""
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)