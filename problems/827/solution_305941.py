def qtd_divisores(n):
    """função que dado um numero, retorne a quantidade de divisores que esse numero possui;int-->int"""
    divisores=[]
    for n in range(1, n+1):
        divisores.append(n)
    return len(divisores)