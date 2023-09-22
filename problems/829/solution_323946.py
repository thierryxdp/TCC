def soma_serie(n):
    """Função que calcula e retorna o valor de H com N
    termos onde N é inteiro e dado como entrada.
int -> float"""
    soma = 0
    for elemento in range(n+1):
        soma += 1 / (2 * elemento)
    return round(soma, 2)