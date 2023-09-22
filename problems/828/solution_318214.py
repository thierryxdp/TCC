def primo(n):
    """Função que dado um n° inteiro positivo, verifica se esse n° é primo
    ou não, e retorna um valor booleano;
    int -> bool"""
    numerosPrimos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            numerosPrimos += 1

    if numerosPrimos == 2:
        return True

    else:
        return False