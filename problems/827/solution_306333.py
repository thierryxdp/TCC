def qtd_divisor(n):
    """..."""
    i = 1
    soma = 0
    numero_primos = 0
    while numero_primos<n:
        if primo(i):
            soma = soma + i
            numero_primos = numero_primos+1
    i = i+1
    return soma