def qtd_divisores(n):
    """Função que  conta quantos divisores um numero dado possui
    int -> int"""
    for divisor in range(1 , n+1):
        if n % divisor == 0:
return divisor