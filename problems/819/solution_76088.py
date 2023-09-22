def filtraMultiplos (numeros, n):
    """funçao que recebe uma lista de numeros, um numero n e retorna uma lista com todos os numeros multiplos de n;
entrada: list, int;
saida: list."""

    multiplos = []
    indice = 0

    while indice <= len (numeros):
        if numeros [indice] % n == 0:
            multiplos = multiplos + [numeros [indice]]
        indice = indice + 1

    return multiplos