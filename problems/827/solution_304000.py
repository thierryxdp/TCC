def qtd_divisores(n):
    """Função que conta quantos divisores o número n tem
       int -> int"""
    numeros = list(range(1,n+1))
    divisores = 0
    for cadaNumero in numeros:
        if n%cadaNumero == 0:
            divisores = divisores + 1
    return divisores