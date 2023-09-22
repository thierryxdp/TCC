def qtd_divisores(n):
    """Essa função retorna a quantidade de divisores de um numero"""
    """int->int"""
    divisores=[]
    for i in range(1,n+1):
        if (n%i) == 0:
            list.append(divisores,i)
    return len(divisores)