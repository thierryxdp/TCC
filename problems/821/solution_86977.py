def fatorial (x):
    """Funçao que recebe um numero x e retorna o fatorial dele;
entrada: int;
saida: int."""
    n = list (range (1, x + 1))
    list.reverse (n)
    pos = 0
    vezes = 1

    while pos < len (n):
        vezes *=  n[pos]
        pos += 1
    return vezes