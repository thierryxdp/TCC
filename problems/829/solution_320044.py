def soma_h(N:int) -> float:
    """Função calcula o valor de h dado por 1 + 1/2 + 1/3 + ... + 1/N

       Parameters:
       N: número inteiro positivo qualquer, valor que assumirá o último
       denominador da série

       Returns:
       Valor de H com duas casas decimais
    """
    H = 0

    for denominador in range(1,N+1):
        H += 1/denominador

    return round(H,2)