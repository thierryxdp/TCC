def qtd_divisores(n):
    divisores = 1
    for divisores in range(1,n+1):
        if n % divisores == 0:
    divisores += 1
    return divisores
        else:
            lista2 = n//divisores
        return lista2