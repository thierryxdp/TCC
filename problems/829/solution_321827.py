def soma_h(N):
    """Função que retorna o valor H com N termos, onde N é o número dado como entrada
int -> float"""

    soma = 0

    for elemento in range(1, N + 1):
        soma = soma + (1/elemento)
    return round(soma, 2)