def qtd_divisores(n):
    lista = list(range(1,n+1))
    divisores = []
    for i in lista:
        if n % i == 0:
            divisores.append(i)
    return len(divisores)