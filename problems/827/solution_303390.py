def qtd_divisores(n):
    """Retorna quantos divisores um número tem; int -> int."""
    divisores= 0
    for i in range(1,n+1):
        if n%i == int:
            divisores= divisores + 1
    return divisores