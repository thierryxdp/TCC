def qtd_divisores(n):
    """Função que retorna quantos divisores tem um determinado
    número."""
    for i in range(1,n/2+1):
        if (n % i) == 0:
    return i