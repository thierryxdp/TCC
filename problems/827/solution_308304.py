def qtd_divisores(n):
    divisores = []
    for i in range(n):
        if n%i==0:
            divisores.append(i)
    return len(divisores)