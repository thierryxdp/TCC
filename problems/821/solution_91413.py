def fatorial(n):
    """Recebe como parâmetro um número n e retorna o fatorial de n;
    assinatura: int --> int
    Casos de teste:
    fatorial(4) == 24
    fatorial(3) == 6"""
    i = 1
    z = n
    while (n - i) > 0:
        z = z * (n - i)
        i += 1
    return z