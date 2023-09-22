def soma_H(N):
    """Função que calcula uma soma do tipo 1 + 1/2 + 1/3 + 1/4 + ... + 1/N para um N inteiro.
    int -> float """

    soma = 0

    for numero in range(1, N + 1):
        if numero != 0:
            soma = soma + 1/numero


    return round(soma, 2)