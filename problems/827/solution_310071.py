def qtd_divisores(n):
    """Função que retorna quantos divisores tem um determinado
    número."""
    for divisor in range (1,n + 1):
        if n % divisor == 0:
            return (divisor)