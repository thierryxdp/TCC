def primo(n):
    lista = list(range(1,n+1))
    divisores = 0
    for i in lista:
        if n % i == 0:
            divisores = divisores + 1
    if divisores > 2:
        return False
    return True