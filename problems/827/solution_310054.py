def qtd_divisores(n):
    """Função que conta quantos divisores um número tem.
    int -> int"""
    for i in range(1, num//2+1):
        if num % i == 0: 
            return i
    return num