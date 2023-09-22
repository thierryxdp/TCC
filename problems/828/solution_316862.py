def primo(numero):
    """
    função que recebe um numero inteiro positivo e verifica se ele é primo ou não, 
    caso seja, retorna "True", caso não seja, retorna "False".
    int--->bool
    """
    primos = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            primos += 1

    if primos == 2:
        return True

    else:
        return False