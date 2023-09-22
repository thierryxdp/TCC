def qtd_divisores(n):
    """Recebe um número e retorna a quantidade de divisores desse número;
    int -> int"""
    divisores = []
    for numero in range(n+1):
        if n%numero == 0:
            divisores.append(numero)
    return len(divisores)