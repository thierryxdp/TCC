def total(x,y):
    soma = 0
    c = 0
    for c in range(len(x)):
        soma = soma + y[x[c]]
    return soma