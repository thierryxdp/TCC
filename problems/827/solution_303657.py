def qtd_divisores(n):
    """Dado um número 'n', a função retorna a quantidade de  divisores
    desse número;
    int -> int"""
    quantidade = []

    for x in range(1,abs(n)+1):
        if (n >=0) and (n%x == 0):
            list.append(quantidade,x)
            qtd = len(quantidade)
        else:
            qtd = 0
    return qtd