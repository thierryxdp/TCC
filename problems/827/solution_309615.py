def qtd_divisores(n):
    """Função que dado um número n, retorna quantos divisores
    este número tem;
    int -> int"""
    i = 0
    for num in range(1, n+1):
        if n%num == 0:
            i = i + 1
    return i