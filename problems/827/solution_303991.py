def qtd_divisores(n):
    """Função que conta quantos divisores o número n tem
       int -> int"""
    numeros = list(range(n+1))
    del numeros[0]
    divisores = 0
    for cadaNumero in numeros:
        if n%cadaNumero == 0:
            divisores = divisores + 1
            return divisores
        else:
        return 0