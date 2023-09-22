def primo(n):
    '''Verifica se n é primo
    int --> bool'''

    # Para identificar a primalidade de um número,
    # basta verificar se existe um número
    # menor ou igual à raiz quadrada dele que o divida
    ponto_parada = round(n**(1/2)) + 1

    # itera pelo intervalo de 2 a 1 mais a raiz quadrada de n
    for i in range(2, ponto_parada):
        # verifica se i é divisor de n
        if n % i == 0:
            # n não é primo
            return False
    # n é primo
    return True