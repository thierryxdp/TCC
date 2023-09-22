def primo(n: int)-> bool:
    """Dado um número inteiro positivo (n), a função verifica se esse número
    é primo ou não"""
    divisores = list()
    for numero in range(1, n+1):
        if (n % numero == 0):
            list.append(divisores, numero)
    if len(divisores) > 2:
        return False
    else:
        return True