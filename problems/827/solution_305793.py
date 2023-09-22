def qtd_divisores(n: int) -> int:
    divisores = 0
    
    for numero in list(range(1, n)):
        if numero % n == 0:
            divisores += 1
    
    return divisores