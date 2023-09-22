def qtd_divisores(n):
    """ Função que conta o número de divisores.
    int, int->int """
    n += 1
    divSum = [1] * n
    divSum[0], divSum[1] = 0, 0
    for i in range(2, n//2+1):
        for j in range(i+i,n,i):
            divSum[j] += i
    return divSum