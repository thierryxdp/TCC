def soma_h(n):
    soma = 0
    for i in range(1,n):
        if i == 0:
            continue
        soma += 1/i
	soma = round (soma,2)
    return soma