def soma_h(x):
    """Função que dado um número inteiro N, calcula e retorna
    o valor H com N termos.
    int->float
    """
    soma = 1
    for numeros in range(2, x + 1):
        soma += 1/numeros
    return round(soma, 2)