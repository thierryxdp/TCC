def soma_h(n):
    soma = 0
    for x in list(range(n)):
        if x > 0:
        	soma = soma + (1/x)
    return round(soma, 2)