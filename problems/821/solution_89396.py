def fatorial(n):
    """
    Calcula e retorna o fatorial de um numero;
    int -> int
    """
    fat = 1
    while n >= 1:
        fat = fat * n
        n = n - 1
    return fat