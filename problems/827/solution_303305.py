def qtd_divisores(n):
    """Esta é a função que dado um número retorna quantos divisores esse número possui, int -> int"""
    divisores = 0

    for x in range(1,n+1):
        if n%x == 0:
            divisores = divisores + 1
            
    return divisores