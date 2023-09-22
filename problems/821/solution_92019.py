def fatorial(n):
    """Recebe um valor inteiro n e calcula  n!
    assinatura: int --> int
    """
    fim=n
    for n in range(1, n):
        fim=fim*n