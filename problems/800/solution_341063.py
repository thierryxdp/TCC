def total(ls, d):
    soma = 0
    for item in ls:
        soma = soma + d[item]
    return soma + 0.00000001