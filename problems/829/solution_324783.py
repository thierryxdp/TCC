soma_h(x):
    soma = ()
    for n in range(1, x):
    	soma = soma + (1/n, )
    res = sum(soma)
    return round(res, 2)