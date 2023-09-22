def qtd_divisores (n):
    """funçao que recebe um numero n e retorna quantos divisores ele possui;
entrada: int;
saida: int."""
    soma = 0
    for i in range (1, n+1):
        if i % n == 0:
            soma = soma + 1

    return soma