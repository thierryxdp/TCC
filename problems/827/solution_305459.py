def qtd_divisores(n):
    """a função encontra quais são divisores de n, caso n seja negativo ele retorna 0, caso seja positivo ele retorna a quantidade de divisores que o valor n tem"""
    divisores = list()
    divisores.append(n)
    if n < 0:
        return 0
    else:
        for i in range(1, int(n/2+1)):
            if n % i == 0:
                divisores.append(i)
        return len(divisores)