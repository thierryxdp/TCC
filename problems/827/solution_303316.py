def qtd_divisores(n):
    """Função que dado um número inteiro 'n' retorna quantos divisores ele tem;
    int -> int"""
    divisores=0
    for e in range(1, n+1):
        if n%e == 0:
            divisores+=1
    return divisores