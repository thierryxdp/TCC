def soma_h(n):
    soma = 1
    if (n == 0):
        return soma
    else:
        for i in range(2, n + 1):
        	soma += 1/n
        return soma