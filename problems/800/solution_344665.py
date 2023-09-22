def total(x, y):
    soma = 0
    c = 0
    for c in range(lange(x)):
        soma = soma + y[x[c]]
    return round(soma, 2)