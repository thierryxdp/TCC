def soma_h(n):
    soma = 1
    if (n == 0):
        return round(soma,2)
    else:
        for i in range(2, n + 1):
        	soma += 1/n
        return round(soma,2)