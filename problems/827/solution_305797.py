def qtd_divisores(n: int) -> int:
    divisores = 0
    
    for numero in list(range(0, n+1)):
        if numero % n == 0:
            divisores = divisores + 1
    
    return divisores