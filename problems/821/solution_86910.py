def fatorial (n):
    """Funçao que recebe um numero n e retorna o fatorial desse numero;
entrada: int;
saida: int."""

    nums = list (range (1, n + 1))
    list.reverse (nums)

    pos = 0
    multiplicar = 1

    while pos < len (nums):
        multiplicar = multiplicar * nums [pos]
        pos = pos + 1
    return multiplicar