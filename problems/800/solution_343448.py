def total(lista, precos):
    soma = 0
    for i in lista:
        p=dict.get(precos, i)
        soma = soma + p
    round(soma,2)
    return soma