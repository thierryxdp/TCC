def qtd_divisores (numero):
    """funçao que recebe um numero inteiro e retorna quantidade de divisores desse numero;
entrada: int;
saida: int."""
    soma = 0
    for elemento in range (1, n+1):
        if n % elemento == 0:
            soma += 1
    return soma