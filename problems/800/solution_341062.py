def total(ls, d):
    soma = 0
    for item in ls:
        soma = soma + d[item]
    return round(soma, 2)