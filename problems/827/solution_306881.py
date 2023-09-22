def qtd_divisores(n):
    """Recebe um número e retorna uma lista com todos os divisores
    desse número;
    int -> list"""
    divisores = []
    for numero in range(1, n+1):
        if n%numero == 0:
            divisores.append(numero)
    return divisores