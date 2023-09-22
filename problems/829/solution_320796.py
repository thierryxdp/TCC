def soma_h(n):
    """
    int->float
    :param n: Entrada do ultimo termo da soma
    :param return: Retorna o valor h com 2 casas decimais.
    """
    lista = range(n+1)
    soma = 0
    for count in lista:
        if count !=0:
            soma = soma + 1/count
    return round(soma,2)