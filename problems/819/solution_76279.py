def filtraMultiplos (lista, x):
    """funçao que recebe uma lista de numeros e um numero x e retorna uma lista com os multiplos de x;
entrada: list, int;
saida: list."""
    nums = []
    pos = 0
    while pos < len (lista):
        if lista[pos] % x == 0:
            nums += [lista [pos]]
        pos += + 1

    return nums