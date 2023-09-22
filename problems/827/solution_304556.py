def divisores(num):
    """Esta funcão conta quantos divisores o numero que é passado como entrada tem."""
    soma = 0
    for d in range(1,num+1):
        if num % d == 0:
            soma = soma + 1
    return soma