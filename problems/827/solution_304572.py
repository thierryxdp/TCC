def qtd_divisores(n):
    """função na qual retorna todos os divisores de um numero"""
    divisores =[]
    for x in range(1,n+1):
        div = n / x
        if n % x == 0:
            list.append(divisores,x)
    return len(divisores)