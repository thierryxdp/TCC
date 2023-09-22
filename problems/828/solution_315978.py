def primo(x):
    """Função que dado um número inteiro positivo, verifica se esse número
    é primo ou não.
    int->bool
    """
    lista = []
    for divisor in range(1, x + 1):
        if x % divisor == 0:
            lista = lista + [divisor]
    if lista == [1, x]:
        return True
    else:
        return False