def qtd_divisores(n):
    """Dado um número 'n', a função retorna a quantidade de  divisores
    desse número;
    int -> int"""
    quantidade = []

    for x in range(1,n+1):
        if n%x == 0:
            list.append(quantidade,x)
            qtd = len(quantidade)
    return qtd