def qtd_divisores(n):
    a = []
    i = 1
    while i <= n:
        if n%i == 0:
            a = a + [i]
        i = i + 1
    return len(a)

def primo(n):
    """Dado um número n,checa se ele é primo"""
    if qtd_divisores(n) == 2:
        return True
    else:
        return False