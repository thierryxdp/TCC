def qtd_divisores(n):
    """funcao que retorna a quantidade de divisores que o numero n tem"""
    """int->int"""
    divisores=0
    lista = list(range(1,n+1))
    for elemento in lista:
        if n%elemento==0:
            divisores=divisores+1
    return divisores